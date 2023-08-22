from db import db

#id, name, sallary, age, designation, yearsofwork

class EmpModel(db.Model):
    __tablename__ = "Employees"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    sallary = db.Column(db.Float)
    age = db.Column(db.Integer)
    designation = db.Column(db.String(20))
    yow = db.Column(db.Integer)

    def __init__ (self, name,sallary, age, designation, yow):
        self.name = name
        self.age = age
        self.sallary = sallary
        self.designation = designation
        self.yow = yow

    def __repr__(self):
        return f"NAME: {self.name} AGE: {self.age} SALLARY: {self.sallary} DESIGNATION: {self.designation}\n"
