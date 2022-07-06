import json
import random

def distance(x1, y1, x2, y2):
    """
    Function get coordinates of two points and returns a distance between them
    AB = √(x2 - x1)2 + (y2 - y1)2
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    print('First of all,here is a formula:')
    print('AB = √(x2 - x1)2 + (y2 - y1)2')
    Distance_betwen_AB = (((x2 - x1) ** 2) + ((y2 - y1) ** 2))**0.5
    return Distance_betwen_AB
functools = distance(5, 150, 150, 5)
print(f'The distance is: {functools}')
print('-' * 30)

def quadratic_equation(a, b, c):
    """
    Return the roots of the quadratic equation
    a * x^2 + b*x + c = 0
    :param a: first argument, couldn't not be 0
    :param b: second argument
    :param c: third argument
    :return: square equation roots
    """
    assert a != 0
    print('First of all,type here the example: ')
    print('a * x^2 + b*x + c = 0')
    discriminant = b ** 2 - 4 * a * c
    print('The discriminant is:' + ' ' + str(discriminant))
    if discriminant == 0:
        x = 'x = ' + str(-b / 2 * a)
        return x
    elif discriminant < 0:
        result = 'It is imposibble '
        return result
    else:
        x1 = ((-b + discriminant ** 0.5) / 2 * a)
        x2 = ((-b - discriminant ** 0.5) / 2 * a)
    return x1, x2


x1, x2 = quadratic_equation(1, 12, 13)
print(x1, x2)
print('-' * 30)


def is_admin(user: dict) -> bool:
    """
    Gets a user and return if the user is admin or not
    User is a dict, the info about user admin status may be present in fields:
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param user: dictionary with user info
    :return: True or False
    """
    admin_being = False
    if 'is_admin' in user:
        admin_being = user.get('is_admin')
    elif 'admin' in user:
        admin_being = user.get('admin')
    elif 'super_user' in user:
        admin_being = user.get('super_user')
    elif 'superuser' in user:
        admin_being = user.get('superuser')
    elif 'is_root' in user:
       admin_being = user.get('is_root')
    elif 'root' in user:
        admin_being = user.get('root')
    return admin_being

    print('-' * 30)

def generate_email(names, domains):

    """
    Даны списки names и domains (создать самостоятельно).
    Написать функцию для генерирования e-mail в формате:
    фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
    фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
    Строку и число генерировать случайным образом.

    Пример использования функции:
    names = ["king", "miller", "kean"]
    domains = ["net", "com", "ua"]
    e_mail = create_email(domains, names)
    print(e_mail)
    ">>>miller.249@sgdyyur.com""
    """

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    mail_name = ''
    for x in range(5, 8):
        mail_name += random.choice(letters)
    email = f'{random.choice(names)}.{random.choice(range(100, 1000))}@{mail_name}.{random.choice(domains)}'
    return email
    names = ['ustynov', 'biden', 'zelenskiy', 'jhonson']
    domains = ['net', 'com', 'ua']
    a = generate_email(names, domains)
    print(f'e-mail address: {a}')
    print('-' * 30)

def find_product(all_products, search_word):
    """
    Create a function to search among products and find by keywords
    :param all_products: iterable of some products
    :param search_word: string to search in product name or product description, case-insensitive
    :return: list of products
    """
    search_word1 = str.lower(search_word)
    found = []
    for item in all_products:
        if search_word1 in str.lower(item['title']):
            found.append(item)
        elif search_word1 in str.lower(item['description']):
            found.append(item)
        elif search_word1 in str.lower(item['brand']):
            found.append(item)
        if len(found) == 0:
            found = 'Try again... '
    return f'I have just found the "{search_word}" and  {found}'
def write_user_to_file(users, search_name):
    """
    Write a function, that takes a user_name or last name find the user and write the result
    to a file <FirstName_LastName>.txt
    The user data inside should be written in a pretty format:

    Key     :       Value
    :param users: iterable of users
    :param search_name: First or Last name of the user to search, case insensitive
    :return:  str file_name of the user if found or empty string if not
    """
    found = []
    new_filename = ''
    for user in users:
        if search_name == user['firstName'] or search_name == user['lastName']:
            found.append(user)
            f_name = user['firstName']
            l_name = user['lastName']
            new_filename = f'{f_name}_{l_name}'
            return f'File "{new_filename}.txt" was created'
        else:
            return new_filename
    pass


if __name__ == '__main__':
    with open('../lesson_7/users.json') as js:
        data = json.load(js)
    users = data.get('users')
    for user in users:
        resultik = is_admin(user)
        print(f'User: {user.get("firstName")} is admin?He/She is - {resultik}')

    with open('products.json') as js:
        data = json.load(js)
    products = data.get('products')
    search = 'Apple'
    staff = find_product(products, search)
    print(staff)