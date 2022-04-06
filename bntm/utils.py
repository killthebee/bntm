import os
import json

from web3 import Web3
from binascii import hexlify

from bntm.settings import INFURIA_NODE, CONTRACT_ADDRESS


def create_hash():
    return str(hexlify(os.urandom(10)), "ascii")


def get_w3_instance():
    return Web3(Web3.HTTPProvider(INFURIA_NODE))


def get_contract(w3=get_w3_instance()):
    with open("abi.json", "r") as abi:
        contract_abi = json.loads(abi.read())
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)
    return contract
