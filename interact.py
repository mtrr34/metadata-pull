import os
import json
from dotenv import load_dotenv
from pathlib import Path
from web3 import Web3, HTTPProvider

f = open("abi.json")
abi = json.load(f)["abi"]
address = "0x95784F7b5c8849b0104EAf5D13d6341d8CC40750"

load_dotenv()

node_provider = os.environ["NODE_API"]
w3 = Web3(HTTPProvider(node_provider))

contract_instance = w3.eth.contract(address=address, abi=abi)

print(contract_instance.functions.ownerOf(1).call())


print(w3.eth.blockNumber)
