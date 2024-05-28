from web3 import Web3
from config import Config

web3 = Config.init_web3()
contract = Config.load_contract(web3)
owner_address = web3.to_checksum_address(Config.OWNER_ADDRESS)
private_key = Config.PRIVATE_KEY

def get_all_records():
    try:
        records = contract.functions.getAllRecords().call()
        formatted_records = []
        for record in records:
            formatted_records.append({
                'student_name': record[0],
                'course': record[1],
                'grade': record[2]
            })
        return formatted_records
    except Exception as e:
        print(f"Erro ao recuperar registros: {e}")
        return []

def add_record(student_name, course, grade):
    tx = contract.functions.addRecord(student_name, course, grade).build_transaction({
        'from': owner_address,
        'nonce': web3.eth.get_transaction_count(owner_address),
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash
