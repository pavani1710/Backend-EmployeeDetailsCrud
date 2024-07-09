# from flask import request, jsonify, current_app as app # type: ignore
# from . import db 
# from .models import Employee


# @app.route('/employees', methods=['GET'])
# def get_employees():
#     employees=Employee.query.all()
#     return jsonify([{'id' : employee.id, 'firstName': employee.firstName, 'lastName':employee.lastName, 'emailId': employee.emailId} for employee in employees])

# @app.route('/employees/<int:id>', methods=['GET'])
# def get_employee(id):
#     employee=Employee.query.get_or_404(id)
#     return jsonify({'id' : employee.id, 'firstName': employee.firstName, 'lastName':employee.lastName, 'emailId': employee.emailId})


# @app.route('/employees', methods=['POST'])
# def create_employee():
#     data=request.get_json()
#     new_employee= Employee(firstName=data['firstName'], lastName=data['lastName'], emailId=data['emailId'])
#     db.session.add(new_employee)
#     db.session.commit()
#     return jsonify({'id': new_employee.id, 'firstName':new_employee.firstName,  'lastName':new_employee.lastName, 'emailId': new_employee.emailId }),201


# @app.route('/employees/<int:id>', methods=['PUT'])
# def update_employee(id):
#     employee= Employee.query.get_or_404(id)
#     data= request.get_json()
#     employee.firstName=data['firstName']
#     employee.lastName=data['lastName']
#     employee.emailId=data['emailId']
#     db.session.commit()
#     return jsonify({'id': employee.id, 'firstName':employee.firstName,  'lastName':employee.lastName, 'emailId': employee.emailId })



# @app.route('/employees/<int:id>', methods=['DELETE'])
# def delete_employee(id):
#     employee= Employee.query.get_or_404(id)
#     db.session.delete(employee)
#     db.session.commit()
#     return '', 204  



from flask import request, jsonify, current_app as app
from . import db
from .models import Employee


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{'id': employee.id, 'firstName': employee.firstName, 'lastName': employee.lastName, 'emailId': employee.emailId} for employee in employees])

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify({'id': employee.id, 'firstName': employee.firstName, 'lastName': employee.lastName, 'emailId': employee.emailId})

@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = Employee(firstName=data['firstName'], lastName=data['lastName'], emailId=data['emailId'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'id': new_employee.id, 'firstName': new_employee.firstName, 'lastName': new_employee.lastName, 'emailId': new_employee.emailId}), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.get_json()
    employee.firstName = data['firstName']
    employee.lastName = data['lastName']
    employee.emailId = data['emailId']
    db.session.commit()
    return jsonify({'id': employee.id, 'firstName': employee.firstName, 'lastName': employee.lastName, 'emailId': employee.emailId})

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return '', 204





