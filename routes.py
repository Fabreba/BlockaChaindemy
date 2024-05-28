from flask import Blueprint, request, render_template, redirect, url_for
from contract import get_all_records, add_record, owner_address

main_blueprint = Blueprint('main', __name__)

requests = []

@main_blueprint.route('/')
def index():
    records = get_all_records()
    message = request.args.get('message')
    return render_template('index.html', owner_address=owner_address, records=records, message=message)

@main_blueprint.route('/add_record', methods=['POST'])
def add_record_route():
    user_address = request.form['user_address']
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
        return redirect(url_for('main.index', message="Solicitação enviada ao proprietário"))
    else:
        tx_hash = add_record(student_name, course, grade)
        return redirect(url_for('main.index', message=f"Record added. Transaction hash: {tx_hash.hex()}"))

@main_blueprint.route('/get_requests')
def get_requests():
    return render_template('requests.html', requests=requests)
