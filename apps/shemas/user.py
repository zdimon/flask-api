from flasgger import Schema, fields

class User(Schema):
    name = fields.Str()
    username = fields.Str()
    password = fields.Str()
