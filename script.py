import requests
import threading
import sys

print(sys.argv)

url = sys.argv[1]
output_arg = sys.argv[2]
n_threads = sys.argv[3]


def task1():
    thread1_loc = 0
    while thread1_loc <= 1500:
        res = requests.get(url + str(thread1_loc)).json()
        print(res["attributes"][2], res[output_arg])
        thread1_loc += 1

def task2():
    thread2_loc = 1501
    while thread2_loc < 3000:
        res = requests.get(url + str(thread2_loc)).json()
        print(res["attributes"][2], res["id"])
        thread2_loc += 1

def task3():
    thread3_loc = 3001
    while thread3_loc < 4500:
        res = requests.get(url + str(thread3_loc)).json()
        print(res["attributes"][2], res["id"])
        thread3_loc += 1

def task4():
    thread4_loc = 4501
    while thread4_loc < 6000:
        res = requests.get(url + str(thread4_loc)).json()
        print(res["attributes"][2], res["id"])
        thread4_loc += 1

def task5():
    thread5_loc = 6001
    while thread5_loc < 7500:
        res = requests.get(url + str(thread5_loc)).json()
        print(res["attributes"][2], res["id"])
        thread5_loc += 1

def task6():
    thread6_loc = 7501
    while thread6_loc < 9599:
        res = requests.get(url + str(thread6_loc)).json()
        print(res["attributes"][2], res["id"])
        thread6_loc += 1

t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')  
t3 = threading.Thread(target=task3, name='t3')  
t4 = threading.Thread(target=task4, name='t4')
t5 = threading.Thread(target=task5, name='t5')  
t6 = threading.Thread(target=task6, name='t6')

# starting threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
  
# wait until all threads finish
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
