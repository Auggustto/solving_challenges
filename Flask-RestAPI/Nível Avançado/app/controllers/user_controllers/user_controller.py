from models.user_models.users_models import UserManager
from dateutil import parser

class UserController:

    def format_birthdata(birthdata):
        return parser.parse(birthdata, dayfirst=True).date()

    
    def create_users(name, lastname, birthdata, email, password):
        object_data = UserController.format_birthdata(birthdata)
        
        return UserManager.create_user(name=name, lastname=lastname, birthdata=object_data, email=email, password=password)
    

    def read_users(email):
        return UserManager.read_user(email=email)


    def update_user(name, lastname, birthdata, email):
        object_data = UserController.format_birthdata(birthdata)

        return  UserManager.update_user(name=name, lastname=lastname, birthdata=object_data, email=email)

    
    def delete_user(email):
        return UserManager.delete_user(email)
    
    
    def all_users():
        return UserManager.read_all_users()

