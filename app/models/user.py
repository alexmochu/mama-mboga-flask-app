from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, name, email, password):
        self.password_hash = generate_password_hash(password)
        self.name = name
        self.id = email

        def ___name__(self):
            return self.name

        def verify_password(self, password):
            return check_password_hash(self.password_hash, password)
