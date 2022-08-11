from app.model.products import Products
from app import response, db
from flask import request

def index():
    try:
        products = Products.query.all()
        data = format_to_array(products)

        return response.success(data=data, msg="List products", code=200)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def detail(id):
    try:
        product = Products.query.filter_by(id=id).first()
        if not product:
            return response.client_error(msg="Product not found", code=400)
        
        data = format_to_object(product)

        return response.success(data=data, msg="Get product", code=200)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def store():
    try:
        code = request.form.get('code')
        name = request.form.get('name')
        description = request.form.get('description')
        category_id = request.form.get('category_id')

        product = Products(code=code, name=name, description=description, category_id=category_id)

        db.session.add(product)
        db.session.commit()

        data = format_to_object(product)

        return response.success(data=data, msg="Store product", code=201)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def update(id):
    try:
        code = request.form.get('code')
        name = request.form.get('name')
        description = request.form.get('description')
        category_id = request.form.get('category_id')

        product = Products.query.filter_by(id=id).first()
        if not product:
            return response.client_error(msg="Product not found", code=400)
        
        product.code = code
        product.name = name
        product.description = description
        product.category_id = category_id
        db.session.commit()

        data = format_to_object(product)

        return response.success(data=data, msg="Update product", code=200)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def destroy(id):
    try:
        product = Products.query.filter_by(id=id).first()
        if not product:
            return response.client_error(msg="Product not found", code=400)
        
        db.session.delete(product)
        db.session.commit()

        return response.success(data=[], msg="Destroy product", code=204)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def format_to_array(datas):
    ret = []
    for item in datas:
        ret.append(format_to_object(item))
    
    return ret

def format_to_object(data):
    ret = {
        'id': data.id,
        'code': data.code,
        'name': data.name,
        'description': data.description,
        'category_id': data.category_id
    }

    return ret