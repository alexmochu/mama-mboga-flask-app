from app.exceptions import UserAlreadyExist, UserDoesNotExist

class Accounts(object):
    """ Creates an Account where users can be stored """

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.id in self.users:
            raise UserAlreadyExist
        else:
            self.users.update({user.id: user})
            
    def remove_user(self, email):
        """This Method removes a user from users dictonary using his/her
        unique email"""
        try:
            self.users.pop(email)
        except KeyError:
            raise UserDoesNotExist

    def check_user(self, email):
        if email in self.users:
            return self.users[email]

    def all_users(self):
        return self.users