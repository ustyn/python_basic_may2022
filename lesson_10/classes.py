import datetime
import json
import random
import string


class User:
    def __init__(self, first_name, last_name, info=None):
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
        self.password = self.generate_password()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def print_me(self):
        print(f'I am {self.__str__()}.')

    def has_admin_role(self):
        # todo: improve this method according to lesson9 home task - read values of all possible "admin"-keys
        if self.info is not None and isinstance(self.info, dict):
            return self.info.get('superuser', False)
        return False

    @staticmethod
    def generate_password(n=5):
        alphabet = string.ascii_letters + string.digits
        psw = ''.join([random.choice(alphabet) for _ in range(n)])
        return psw

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'USER : {self.first_name} {self.last_name}'

    def __gt__(self, other):
        # self > other
        return self.first_name > other.first_name

    def __lt__(self, other):
        # self < other
        return self.first_name < other.first_name

    def __getitem__(self, item):
        # method allows to call User instance with square brackets:
        # >>> address = user['address']
        return self.info.get(item)


if __name__ == '__main__':
    u1 = User('John', 'Doe')
    u1.print_me()

    u2 = User('Robb', 'Stark')
    u2.print_me()

    u3 = User('Aria', 'Stark')
    print(u3.first_name)
    # u2.get_me()

    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    users = data.get('users')

    admins = []
    user_instance = None
    for user in users:
        firstname = user.get('firstName')
        lastname = user.get('lastName')
        user_instance = User(firstname, lastname, info=user)

        user_instance.print_me()      # print

        if user_instance.has_admin_role():
            print(f'User {user_instance.last_name}  is admin')
            admins.append(user_instance)

    print(f'I found {len(admins)}  admins among users.')
    for admin in admins:
        print(admin)
        admin.password = admin.generate_password(15)
        admin.updated_at = datetime.datetime.now()
        print('New password: ', admin.password)

        # possible but bad practice - better define all attribute inside the class, but not outside
        # admin.new_attribute = 'something'

    random_psw = User.generate_password(7)
    print(random_psw)

    admin1 = admins[0]
    admin2 = admins[-1]
    print(admin1 > admin2)

    sorted_admins = sorted(admins)
    print(sorted_admins)

    address = user_instance['address']
    print(address)

    # print('firstname: ', User.first_name)     # WARNING !!! ERROR :  AttributeError
