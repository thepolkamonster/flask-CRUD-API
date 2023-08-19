from flask import request, render_template
from flask_smorest import Blueprint, abort

blp = Blueprint("views", __name__, description = "Blueprint for views")

@blp.route('/delete')
def delete():
    return render_template("delete.html")

@blp.route('/create')
def create():
    return render_template("create.html")

@blp.route('/update')
def update():
    return render_template("update.html")

@blp.route('/getall')
def getall():
    return render_template("getall.html")

@blp.route('/getone')
def getone():
    return render_template("getone.html")
