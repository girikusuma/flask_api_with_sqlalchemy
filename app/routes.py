from app import app, response
from flask import request, jsonify
from app.controller import categories_controller as CategoryController
from app.controller import products_controller as ProductController
from app.controller import user_controller as UserController
from flask_jwt_extended import get_jwt_identity, jwt_required

@app.route("/")
def index():
    return "Welcome to Flask Application"

@app.route("/register/", methods=['POST'])
def register():
    if request.method == 'POST':
        return UserController.register()
    else:
        raise Exception("Method not allowed")

@app.route("/login/", methods=['POST'])
def login():
    if request.method == 'POST':
        return UserController.login()
    else:
        raise Exception("Method not allowed")

@app.route("/categories/", methods=['GET', 'POST'])
@jwt_required()
def categories_list():
    if request.method == 'GET':
        return CategoryController.index()
    elif request.method == 'POST':
        return CategoryController.store()
    else:
        raise Exception("Method not allowed")

@app.route("/categories/<int:id>/", methods=['GET','PUT', 'DELETE'])
@jwt_required()
def categories_detail(id):
    if request.method == 'GET':
        return CategoryController.detail(id)
    elif request.method == 'PUT':
        return CategoryController.update(id)
    elif request.method == 'DELETE':
        return CategoryController.destroy(id)
    else:
        raise Exception("Method not allowed")

@app.route("/products/", methods=['GET', 'POST'])
@jwt_required()
def products_list():
    if request.method == 'GET':
        return ProductController.index()
    elif request.method == 'POST':
        return ProductController.store()
    else:
        raise Exception("Method not allowed")

@app.route("/products/<int:id>/", methods=['GET','PUT', 'DELETE'])
@jwt_required()
def products_detail(id):
    if request.method == 'GET':
        return ProductController.detail(id)
    elif request.method == 'PUT':
        return ProductController.update(id)
    elif request.method == 'DELETE':
        return ProductController.destroy(id)
    else:
        raise Exception("Method not allowed")

@app.route("/products-galery/", methods=['POST'])
@jwt_required()
def products_galery():
    if request.method == 'POST':
        return ProductController.upload_galery()
    else:
        raise Exception("Method not allowed")
