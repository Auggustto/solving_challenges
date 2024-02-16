from flask import Flask, request
from flask_restful import Resource, Api

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = "2ibma*<6{8i*]slz5^217p(q4z=&4$xv_d_:[)j=+=24[8e!|0{`>634+r[%bg2"
jwt = JWTManager(app)


users = {}
next_user_id = 1


class Login(Resource):
    def post(self):
        """
        Verifica se o e-mail e a senha fornecidos correspondem a um usuário cadastrado.

        Retorna uma mensagem de sucesso se o login for bem-sucedido ou uma mensagem de erro se o e-mail ou a senha estiverem incorretos.

        Returns:
            dict: Mensagem de sucesso ou erro com o status HTTP correspondente.
        """
        email = request.json.get("email")
        password = request.json.get("password")

        for user in users.values():
            if user["email"] == email and user["password"] == password:
                access_token = create_access_token(identity=email)

                return access_token, 200
            
        return {"message": "E-mail or password is incorrect!"}, 401


class Users(Resource):

    @jwt_required()
    def search_user(user_id):
        """
        Busca um usuário pelo ID.

        Args:
            user_id (int): O ID do usuário a ser pesquisado.

        Returns:
            dict or None: As informações do usuário, se encontrado, caso contrário, None.
        """
        if user_id in users:
            return users[user_id]


    @jwt_required()
    def post(self):
        """
        Adiciona um novo usuário.
        """
        user_id = request.json.get("user_id")
        filter_user = Users.search_user(user_id)

        if filter_user:
            return filter_user, 200
        else:
            return {"message": "User not found!"}, 404


    @jwt_required()
    def put(self):
        """
        Atualiza as informações de um usuário existente.
        """
        user_id = request.json.get("user_id")
        fullname = request.json.get("fullname")
        email = request.json.get("email")
        birth_date = request.json.get("birth_date")
        password = request.json.get("password")

        if user_id in users:
            users[user_id].update({
                "fullname": fullname,
                "email": email,
                "birth_date": birth_date,
                "password": password
            })
            return users[user_id], 200
        else:
            return {"message": "User not found!"}, 404


    @jwt_required()
    def delete(self):
        """
        Remove um usuário existente.
        """
        user_id = request.json.get("user_id")

        if user_id in users:
            users.pop(user_id)
            return {"message": f"User {user_id} deleted sucessfully!"}
        else:
            return {"message": "User not found!"}, 404


class ListUsers(Resource):

    @jwt_required()
    def get(self):
        """
        Obtém a lista de todos os usuários.
        """
        return {"users": users}, 200


    def post(self):
        """
        Adiciona um novo usuário à lista.
        """
        global next_user_id

        dados = request.json
        user_id = next_user_id
        users[user_id] = dados
        next_user_id += 1
        return {"message": "User created successfully!"}, 201


api.add_resource(ListUsers, '/api/users')
api.add_resource(Users, '/api/user_methods')
api.add_resource(Login, '/api/login')


if __name__=="__main__":
    app.run(debug=True)
