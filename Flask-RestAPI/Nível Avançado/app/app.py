from flask import Flask, request
from flask_restful import Resource, Api

from controllers.user_controller.user_controller import UserController
from controllers.login_controller.login_controller import LoginController


app = Flask(__name__)
api = Api(app)


class Login(Resource):

    def post(self):
        email = request.json.get("email")
        password = request.json.get("password")

        return LoginController.login_user(email, password)



class User(Resource):

    @staticmethod
    def get_metadata():
        return (
            request.json.get("name"),
            request.json.get("lastname"),
            request.json.get("birthdata"),
            request.json.get("email"),
            request.json.get("password")
        )


    def post(self):
        _, _, _, email, _= self.get_metadata()
        return UserController.read_user(email=email)


    def put(self):
        name, lastname, birthdata, email, _ = self.get_metadata()

        return UserController.update_user(name, lastname, birthdata, email)
    

    def delete(self):
        email = request.json.get("email")

        return UserController.delete_user(email)


class CreateUser(Resource):

    def get(self):
        return UserController.all_users()


    def post(self):
        name, lastname, birthdata, email, password = User.get_metadata()

        return UserController.create_user(name=name, lastname=lastname, birthdata=birthdata, email=email, password=password)



api.add_resource(CreateUser, '/api/create_users')
api.add_resource(User, '/api/users')
api.add_resource(Login, '/api/login')




if __name__ == "__main__":
    app.run(debug=True)