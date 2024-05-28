import os
from web3 import Web3
import json
class Config:
    GANACHE_URL = "http://127.0.0.1:7545/"
    CONTRACT_ADDRESS = "0xF9b4C1d3074935FaC38E04bC874cC077af942926"
    OWNER_ADDRESS = "0x322Bc6562352aa517aC5bb349c82e114cef9B02c"
    PRIVATE_KEY = "0xfbe3eaf8f624fac7b34648af3bdca6533e9327732523014518a6fed342b4499d"

    @staticmethod
    def init_web3():
        return Web3(Web3.HTTPProvider(Config.GANACHE_URL))

    @staticmethod
    def load_contract(web3):
        with open('build/contracts/AcademicRecords.json') as f:
            contract_json = json.load(f)
            contract_abi = contract_json['abi']
        return web3.eth.contract(address=web3.to_checksum_address(Config.CONTRACT_ADDRESS), abi=contract_abi)
