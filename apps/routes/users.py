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
        }
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
       
        return jsonify({'message': 'Ok'})

app.add_url_rule(
    '/user/create',
    view_func=UsersView.as_view('create user'),
    methods=['POST']
)