from app.model.categories import Categories
from app import response, db
from flask import request

def index():
    try:
        categories = Categories.query.all()
        data = format_to_array(categories)

        return response.success(data=data, msg="List categories", code=200)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def detail(id):
    try:
        category = Categories.query.filter_by(id=id).first()
        if not category:
            return response.client_error(msg="Category not found", code=400)
        
        data = format_to_object(category)

        return response.success(data=data, msg="Get category", code=200)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def store():
    try:
        code = request.form.get('code')
        name = request.form.get('name')
        description = request.form.get('description')

        category = Categories(code=code, name=name, description=description)

        db.session.add(category)
        db.session.commit()

        data = format_to_object(category)

        return response.success(data=data, msg="Store category", code=201)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def update(id):
    try:
        code = request.form.get('code')
        name = request.form.get('name')
        description = request.form.get('description')

        category = Categories.query.filter_by(id=id).first()
        if not category:
            return response.client_error(msg="Category not found", code=400)
        
        category.code = code
        category.name = name
        category.description = description
        db.session.commit()

        data = format_to_object(category)

        return response.success(data=data, msg="Update category", code=200)
    except Exception as e:
        return response.server_error(msg="Fail: "+str(e), code=500)

def destroy(id):
    try:
        category = Categories.query.filter_by(id=id).first()
        if not category:
            return response.client_error(msg="Category not found", code=400)
        
        db.session.delete(category)
        db.session.commit()

        return response.success(data=[], msg="Destroy category", code=204)
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
        'description': data.description
    }

    return ret