import bcrypt


class HashModels:

    def hash(password):

        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

        return password_hash