"""
    1° CRUD de postagens
    2° incluindo a capacidade de filtrar por diferentes critérios, como data de publicação, autor, categoria, etc.
    3° Login
        - hashing de senhas
    4° autenticação

"""
from db.database import session, User
from models.hash_models.hash_model import HashModels

class User_Methods:

    def filter_users(email):
        return session.query(User).filter_by(email=email).first()


    def create(name, lastname, birthdata, email, password):
        try:
            existing_user = User_Methods.filter_users(email=email)

            if existing_user:
                return {"message": f"Email {email} is already in use!"}, 500
            
            new_user = User(name=name, lastname=lastname, birthdata=birthdata, email=email, password=HashModels.hash(password))
            session.add(new_user)
            session.commit()

            return {"message": "User created sucessfully!"}, 201
            
        except Exception as e:
            session.rollback()
            print("Error occurred during user creation:", e)
            return {"error": str(e)}, 500
        
        
    def read(email):
        try:
            read_user = User_Methods.filter_users(email)
            return read_user.as_dict()
        
        except Exception as e:
            return e, 500


    def update(name, lastname, birthdata, email):
        try:
            select_user = User_Methods.filter_users(email)

            if select_user:
                select_user.name = name
                select_user.lastname = lastname
                select_user.birthdata = birthdata

                session.commit()
                
                return {"message": "User update sucessfully!"}, 200
            
            return {"error": f"User: {email} not found!"}, 500
            
        except Exception as e:
            session.rollback()
            return {"error": str(e)}, 500

    def delete():
        pass