import datetime
import json
import random
import string
import os
from lesson_9.Topal import find_product


class BaseUser:
    def __init__(self, *args, **kwargs):
        pass

    def generate_password(self, *args, **kwargs):
        pass


class User(BaseUser):
    def __init__(self, first_name, last_name, info=None):
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
        # protected attribute with single underscore
        self._password = self.generate_password()       # _protected
        # __private attribute with double underscore
        self.__mac_address = info.get('macAddress') if info is not None else None
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    # decorator property converts a method to an attribute
    # what the difference between attribute and method of the class?
    # you call attribute without braces: user.first_name
    # you call method with braces(): user.print_me()
    # so method is like a function call
    # With property decorator we can use our "method" as an attribute without ():
    # user.mac_address
    # Property can not be assigned, so this will generate an error:
    # user.mac_address = 'another mac address'
    @property
    def mac_address(self):
        return self.__mac_address

    @property
    def password(self):
        return self._password

    # @password.setter
    def set_password(self, psw):
        self._password = psw

    def print_me(self):
        print(f'I am {self.__str__()}.')

    @property
    def has_admin_role(self):
        if self.info is not None and isinstance(self.info, dict):
            key = list(set(self.info.keys()).intersection(
                {'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'})
            )
            if key:
                return self.get(key[0], False)
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


class Customer(User):
    def __init__(self, first_name, last_name, info=None):
        print('Creating customer... ')
        super().__init__(first_name, last_name, info=info)
        self.registered_at = datetime.datetime.now()
        self.basket = list()

    def perform_purchase(self, item):
        self.basket.append(item)

    @property
    def total_value(self):
        return sum([i.get('price', 0) for i in self.basket])

    @property
    def mac_address(self):
        print(f'Customer {self.first_name} requests his mac_addr')
        return super().mac_address

    def set_mac(self, mac_address):
        self.__mac_address = mac_address


def main():
    u1 = User('John', 'Doe')
    u1.print_me()

    u2 = User('Robb', 'Stark')
    u2.print_me()

    u3 = User('Aria', 'Stark')
    print(u3.first_name)
    # u2.get_me()

    with open('lesson_7/users.json') as js:
        data = json.load(js)

    users = data.get('users')

    admins = []
    user_instance = None
    for user in users:
        firstname = user.get('firstName')
        lastname = user.get('lastName')
        user_instance = User(firstname, lastname, info=user)

        user_instance.print_me()  # print

        if user_instance.has_admin_role:  # since has_admin_role is a property, we can use it without braces
            print(f'User {user_instance.last_name}  is admin')
            admins.append(user_instance)
        print('user psw: ', user_instance.password)
        print('user macaddr: ', user_instance.mac_address)

    print(f'I found {len(admins)}  admins among users.')
    for admin in admins:
        print(admin)
        admin.set_password(admin.generate_password(15))
        admin.updated_at = datetime.datetime.now()
        print('New password: ', admin.password)

        # possible but bad practice - better define all attribute inside the class, but not outside
        # admin.new_attribute = 'something'

    # we can call the staticmethod by class name, without an instance of this class
    random_psw = User.generate_password(7)
    print(random_psw)

    admin1 = admins[0]
    admin2 = admins[-1]
    print(admin1 > admin2)

    sorted_admins = sorted(admins)
    print(sorted_admins)

    address = user_instance['address']
    print(address)

    # property demo
    try:
        print('Admin mac address: ', admin1.mac_address)
        print('!!Trying to set property will raise an error!!')
        admin1.mac_address = 'something'
    except Exception as e:
        print('UPS, an error:')
        print(e)
    print('Admin mac address: ', admin1.mac_address)
    print('Now you see that property can not be set this way, mac address is still the same')


if __name__ == '__main__':
    # main()

    customer = Customer('Johnny', 'Depp', {'ex_wife': "Amber  Heardt",
                                           'macAddress': 'JJ:12:DD:A2'})
    customer.print_me()

    customer.perform_purchase({})

    with open('lesson_9/products.json') as js:
        data = json.load(js)
    products = data.get('products')
    search_word = 'watch'
    found_product = find_product(products, search_word)
    if found_product:
        customer.perform_purchase(found_product[0])

    found_iphone = find_product(products, 'iphone')
    if found_product:
        customer.perform_purchase(found_iphone[0])

    print(f'Busket total amount: ${customer.total_value}')

    print('Customer mac: ', customer.mac_address)

