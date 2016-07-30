import os
from flask import send_file

__author__ = 'Aradia'
from app import app


@app.route('/image/<string:id>')

def screenshot(id):
    p = os.path.abspath(os.path.join("/ftp", "id"))
    if os.path.exists(p):
        return send_file(p,  mimetype="image/jpg")
    else:
        return "pososi pisos cyka"
