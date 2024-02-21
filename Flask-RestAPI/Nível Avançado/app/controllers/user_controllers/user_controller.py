from models.user_models.users_models import User_Methods
from dateutil import parser

class User_Controller:

    def Format_Birthdata(birthdata):
        object_data = parser.parse(birthdata, dayfirst=True).date()
        return object_data

    
    def create_users(name, lastname, birthdata, email, password):
        object_data = User_Controller.Format_Birthdata(birthdata)
        create_user = User_Methods.create(name=name, lastname=lastname, birthdata=object_data, email=email, password=password)
        
        return create_user
    

    def read_users(email):
        read_user = User_Methods.read(email=email)

        return read_user
    
    def update_user(name, lastname, birthdata, email):
        object_data = User_Controller.Format_Birthdata(birthdata)
        update_user = User_Methods.update(name=name, lastname=lastname, birthdata=object_data, email=email)
        
        return update_user

