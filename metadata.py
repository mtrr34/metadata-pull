import requests
from threading import Thread
import sys

# Initialize output file
output = open("tokenIds.txt", "w")

# Read in cli arguments
url = sys.argv[1]
collection_size = int(sys.argv[2])
n_threads = int(sys.argv[3])
output_arg = sys.argv[4]

# Calculate the bound size or range for thread argument loop
bound_size = collection_size // n_threads


def task(location, end):
    while location <= end:
        res = requests.get(url + str(location)).json()
        # print(res) -> use this to determine what metadata you want to pull
        if res["attributes"][2]["value"] == "Cyber Ghost":
            output.write(str(res[output_arg]) + "\n")
        location += 1


def getBounds(n):
    res = [0] * 2
    if n + 1 == n_threads:
        res[0] = bound_size * n
        res[1] = collection_size - 1
    else:
        res[0] = bound_size * n
        res[1] = bound_size * (n + 1) - 1
    return res


threads = []
for n in range(n_threads):
    bounds = getBounds(n)
    t = Thread(target=task, args=(bounds[0], bounds[1]))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

output.close()
