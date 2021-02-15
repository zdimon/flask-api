from flasgger import Swagger, SwaggerView
from ..shemas.user import User
from app import app

class UsersView(SwaggerView):
    parameters = [
        {
            "name": "name",
            "type": "string",
            "required": True,
        },
        {
            "name": "username",
            "type": "string",
            "required": True,
        },
        {
            "name": "password",
            "type": "string",
            "required": True,
        },
        {
            "name": "file",
            "type": "file",
            "required": False,
        }
    ]
    consumes = [
        "multipart/form-data"
    ]
    responses = {
        200: {
            "description": "Create user",
            "schema": User
        }
    }

    def post(self):
        """
        
        Creating a new user.

        """
        print(self.request.form)
        return jsonify({'message': 'Ok'})

app.add_url_rule(
    '/user/create',
    view_func=UsersView.as_view('create user'),
    methods=['POST']
)
from flask_restful import Api, Resource

class CreateUser(Resource):
    def get(self, username):
        """
        This examples uses FlaskRESTful Resource
        It works also with swag_from, schemas and spec_dict
        ---
       
        """
        return {'username': username}, 200

