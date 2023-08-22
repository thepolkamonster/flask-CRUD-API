from flask import request, render_template, redirect, url_for
from flask_smorest import Blueprint, abort
from forms import CreateForm, Updateform, DeleteForm, GetOneForm
from models import EmpModel
from db import db

blp = Blueprint("views", __name__, description = "Blueprint for views")

@blp.route('/delete', methods = ['GET','POST'])
def delete():
    form = DeleteForm()

    if form.validate_on_submit():
        id_req = form.id.data
        emp = EmpModel.query.get_or_404(id_req)
        db.session.delete(emp)
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template("delete.html", form = form)

@blp.route('/create', methods = ['GET','POST'])
def create():
    form = CreateForm()

    if form.validate_on_submit():
        emp = EmpModel(name = form.name.data,
                       sallary = form.sallary.data,
                       age = form.age.data,
                       designation=form.designation.data,
                       yow = form.yearsofwork.data)

        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('routes.index'))

    return render_template('create.html',form = form)

@blp.route('/update', methods = ["GET","POST"])
def update():
    form = Updateform()
    if form.validate_on_submit():
        id_req = form.id.data
        name_req = form.name.data
        age_req = form.age.data
        sallary_req = form.sallary.data
        designation_req = form.designation.data
        yow_req = form.yearsofwork.data
        
        emp = EmpModel.query.get(id_req)
        if emp:
            emp.name = name_req
            emp.age = age_req
            emp.sallary = sallary_req
            emp.designation = designation_req
            emp.yow = yow_req
        else:
            emp = EmpModel(id_req, name = name_req, sallary=sallary_req, age = age_req, designation = designation_req, yow = yow_req)
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('routes.index'))

    return render_template("update.html", form = form)

@blp.route('/getall')
def getall():
    res = EmpModel.query.all()
    return render_template("getall.html", res = res)

@blp.route('/getone', methods = ["GET","POST"])
def getone():
    return render_template("getone.html")
