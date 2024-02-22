from models.user_models.users_models import User_Methods
from dateutil import parser

class User_Controller:

    def Format_Birthdata(birthdata):
        return parser.parse(birthdata, dayfirst=True).date()

    
    def create_users(name, lastname, birthdata, email, password):
        object_data = User_Controller.Format_Birthdata(birthdata)
        
        return User_Methods.create(name=name, lastname=lastname, birthdata=object_data, email=email, password=password)
    

    def read_users(email):
        return User_Methods.read(email=email)


    def update_user(name, lastname, birthdata, email):
        object_data = User_Controller.Format_Birthdata(birthdata)

        return  User_Methods.update(name=name, lastname=lastname, birthdata=object_data, email=email)

    
    def delete_user(email):
        return User_Methods.delete(email)
    
    
    def all_users():
        return User_Methods.read_all_users()

