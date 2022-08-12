from importlib.resources import path
from app.model.products import Products
from app.model.product_galeries import ProductGalery
from app import response, db, upload_config, app
from flask import request
import os
import uuid
from werkzeug.utils import secure_filename

def upload_galery():
    try:
        product_id = request.form.get('produc_id')
        title = request.form.get('title')

        if 'file' not in request.files:
            return response.client_error(msg="File not upload", code=400)
        
        file = request.files['file']
        if file.filename == '':
            return response.client_error(msg="File not upload", code=400)
        if file and upload_config.allowed_extentions(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            rename = "Flask-" + str(uid) + filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], rename))

            galery = ProductGalery(product_id=product_id ,title=title, path=rename)
            db.session.add(galery)
            db.session.commit()

            return response.success(data={'image_path': rename}, msg="Success upload image", code=200)
        
        return response.client_error(msg="File extention not allowed", code=400)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

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
        galeries = ProductGalery.query.filter((ProductGalery.product_id == id))
        if not product:
            return response.client_error(msg="Product not found", code=400)
        
        data = format_to_object(product, galeries)

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
        galeries = ProductGalery.query.filter((ProductGalery.product_id == item.id))
        ret.append(format_to_object(item, galeries))
    
    return ret

def format_to_object(data, galery):
    ret = {
        'id': data.id,
        'code': data.code,
        'name': data.name,
        'description': data.description,
        'category_id': data.category_id,
        'galeries': format_to_array_object_galery(galery)
    }

    return ret

def format_to_array_object_galery(datas):
    ret = []

    for item in datas:
        ret.append({
            'path': item.path
        })
    
    return ret