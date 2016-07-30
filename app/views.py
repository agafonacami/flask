import os

__author__ = 'Aradia'
from flask import render_template, send_file
from app import app

@app.route('/image/<string:id>')

def screenshot(id):
    p = os.path.abspath(os.path.join("/ftp", id))
    if os.path.exists(p):
        return send_file(p,  mimetype="image/jpg")
    else:
        return "pososi pisos cyka"



@app.route('/')
@app.route('/index')

def index():
  return render_template("index.html")


