from flask import Flask, request
from flask_restful import Resource, Api

from controllers.user_controllers.user_controller import User_Controller


app = Flask(__name__)
api = Api(app)


class User(Resource):

    def post(self):
        email = request.json.get("email")
        read_user = User_Controller.read_users(email=email)

        return read_user



class CreateUser(Resource):
    def post(self):

        name = request.json.get("name")
        lastname = request.json.get("lastname")
        birthdata = request.json.get("birthdata")
        email = request.json.get("email")
        password = request.json.get("password")

        print(name, lastname, birthdata, email, password)

        create_user = User_Controller.create_users(name=name, lastname=lastname, birthdata=birthdata, email=email, password=password)

        return create_user



api.add_resource(CreateUser, '/api/create_users')
api.add_resource(User, '/api/users_methods')



if __name__ == "__main__":
    app.run(debug=True)