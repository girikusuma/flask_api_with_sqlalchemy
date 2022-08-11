from app.model.user import User, generate_password_hash
from app import response, db
from flask import request

def register():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role') if request.form.get('role') else "admin"

        user = User(name=name, email=email, password=generate_password_hash(password), role=role)
        db.session.add(user)
        db.session.commit()

        data = format_to_object(user)

        return response.success(data=data, msg="Register user admin", code=201)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def format_to_object(data):
    return {
        'name': data.name,
        'email': data.email
    }
    