from models.user_models import User_Methods
from db.database import session

class User_Controller:
    
    def create(name, lastname, birthdata, email, password):
        try:
            create_user = User_Methods.create(name=name, lastname=lastname, birthdata=birthdata, email=email, password=password)
            
            if create_user:
                return {"message": "User created sucessfully!"}, 201
            
        except Exception as e:
            session.rollback()
            return {"error": e}, 500