"""
    1° CRUD de postagens
    2° incluindo a capacidade de filtrar por diferentes critérios, como data de publicação, autor, categoria, etc.
    3° Login
        - hashing de senhas
    4° autenticação

"""
from db.database import session, User
from models.hash_models import HashModels

class User_Methods:

    def filter_users(email):
        return session.query(User).filter_by(email=email).first()


    def create(name, lastname, birthdata, email, password):
        existing_user = User_Methods.filter_users(email=email)

        if existing_user:
            return {"message": f"Email {email} is already in use!"}, 500
        
        else:
            new_user = User(name=name, lastname=lastname, birthdata=birthdata, email=email, password=HashModels.hash(password))
            session.commit()
            return new_user
        

    def read():
        pass


    def update():
        pass


    def delete():
        pass