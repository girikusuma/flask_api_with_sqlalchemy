ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_extentions(filename):
    return '.' in filename and filename.split('.', 1)[1] in ALLOWED_EXTENSIONS