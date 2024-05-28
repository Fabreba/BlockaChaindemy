from flask import Flask, request, render_template, redirect, url_for
from web3 import Web3
import json
import os

app = Flask(__name__)

ganache_url = "http://127.0.0.1:7545/"
web3 = Web3(Web3.HTTPProvider(ganache_url))

contract_address = web3.to_checksum_address("0xF9b4C1d3074935FaC38E04bC874cC077af942926")

with open('build/contracts/AcademicRecords.json') as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

owner_address = web3.to_checksum_address('0x322Bc6562352aa517aC5bb349c82e114cef9B02c')
private_key = '0xfbe3eaf8f624fac7b34648af3bdca6533e9327732523014518a6fed342b4499d'

requests = []

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

@app.route('/')
def index():
    records = get_all_records()
    message = request.args.get('message')
    return render_template('index.html', owner_address=owner_address, records=records, message=message)

@app.route('/add_record', methods=['POST'])
def add_record():
    user_address = web3.to_checksum_address(request.form['user_address'])
    student_name = request.form['student_name']
    course = request.form['course']
    grade = request.form['grade']
    if user_address != owner_address:
        requests.append({
            'user_address': user_address,
            'student_name': student_name,
            'course': course,
            'grade': grade
        })
        return redirect(url_for('index', message="Solicitação enviada ao proprietário"))
    else:
        tx = contract.functions.addRecord(student_name, course, grade).build_transaction({
            'from': owner_address,
            'nonce': web3.eth.get_transaction_count(owner_address),
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei')
        })
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        web3.eth.wait_for_transaction_receipt(tx_hash)
        return redirect(url_for('index', message=f"Record added. Transaction hash: {tx_hash.hex()}"))

@app.route('/get_requests')
def get_requests():
    return render_template('requests.html', requests=requests)

if __name__ == '__main__':
    app.run(debug=True)
