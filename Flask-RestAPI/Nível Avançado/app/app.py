from flask import Flask, request
from flask_restful import Resource, Api

from controllers.user_controllers.user_controller import User_Controller


app = Flask(__name__)
api = Api(app)


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
        read_user = User_Controller.read_users(email=email)

        return read_user


    def put(self):
        name, lastname, birthdata, email, _ = self.get_metadata()
        update_user = User_Controller.update_user(name, lastname, birthdata, email)

        return update_user
    

    def delete(self):
        email = request.json.get("email")
        delete_user = User_Controller.delete_user(email)

        return delete_user



class CreateUser(Resource):

    def get(self):
        return User_Controller.all_users()

    def post(self):
        name, lastname, birthdata, email, password = User.get_metadata()
        return User_Controller.create_users(name=name, lastname=lastname, birthdata=birthdata, email=email, password=password)



api.add_resource(CreateUser, '/api/create_users')
api.add_resource(User, '/api/users')



if __name__ == "__main__":
    app.run(debug=True)