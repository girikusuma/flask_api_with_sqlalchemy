from flask import jsonify, make_response

def success(data, msg, code):
    res = {
        'data': data,
        'message': msg
    }

    return make_response(jsonify(res)), code

def client_error(msg, code):
    res = {
        'message': msg
    }

    return make_response(jsonify(res)), code

def server_error(msg, code):
    res = {
        'message': msg
    }

    return make_response(jsonify(res)), code