from flask import request, render_template
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import EmpModel
from sqlalchemy.exc import SQLAlchemyError
from db import db
from schemas import EmpSchema, EmpUpdateSchema

blp = Blueprint("routes", __name__, description = "The main routes Blueprint")

@blp.route('/')
def index():
    return render_template('index.html')
@blp.route('/api/employee')
class Employee(MethodView):
    @blp.response(200, EmpSchema(many = True))
    def get(self):
        res = EmpModel.query.all()
        return res
    
    @blp.arguments(EmpSchema)
    @blp.response(201, EmpSchema)
    def post(self, emp_data):
        temp_emp = EmpModel(**emp_data)
        try:
            db.session.add(temp_emp)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message = 'Error While Inserting')
        return temp_emp
    
@blp.route('/api/employee/<string:id_req>')
class Empop(MethodView):
    @blp.response(201, EmpSchema)
    def get(self,id_req):
        res = EmpModel.query.get_or_404(id_req)
        return res
    


    @blp.arguments(EmpUpdateSchema)
    @blp.response(200,EmpUpdateSchema)
    def put(self,emp_data, id_req):
        emp = EmpModel.query.get(id_req)
        if emp:
            emp.name = emp_data["name"]
            emp.age = emp_data["age"]
            emp.sallary = emp_data["sallary"]
            emp.designation = emp_data["designation"]
            emp.yow = emp_data["yow"]
        else:
            emp = EmpModel(id = id_req, **emp_data)
        
        db.session.add(emp)
        db.session.commit()

        return emp, 200
    
    @blp.response(200, EmpSchema)
    def delete(self, id_req):
        emp = EmpModel.query.get_or_404(id_req)
        db.session.delete(emp)
        db.session.commit()

        return emp



        
    

            
        


