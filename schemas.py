from marshmallow import Schema, fields

class EmpSchema(Schema):
    id = fields.Integer(dump_only = True)
    name = fields.String(required=True)
    sallary = fields.Float(required = True)
    age = fields.Integer(required = True)
    designation = fields.String(required=True)
    yow = fields.Integer(required = True)

class EmpUpdateSchema(Schema):
    name = fields.String(required=True)
    sallary = fields.Float(required = True)
    age = fields.Integer(required = True)
    designation = fields.String(required=True)
    yow = fields.Integer(required = True)

    