from app.model.user import User
from app import response, db
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime

def register():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role') if request.form.get('role') else "admin"

        user = User(name=name, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        data = format_to_object(user)

        return response.success(data=data, msg="Register user admin", code=201)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.client_error(msg="Email not registered", code=404)
        if not user.check_password(password):
            return response.client_error(msg="Password not match", code=400)

        data = format_to_object(user)

        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        res = {
            'data': data,
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

        return response.success(data=res, msg="Loged in", code=200)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def format_to_object(data):
    return {
        'name': data.name,
        'email': data.email
    }
    