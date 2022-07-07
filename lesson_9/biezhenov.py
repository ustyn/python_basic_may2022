import json
import random
import string


def distance(x1, y1, x2, y2):
    """
    Function get coordinates of two points and returns a distance between them
    :param x1: x-coordinate of point 1
    :param y1: y-coordinate of point 1
    :param x2: x-coordinate of point 2
    :param y2: y-coordinate of point 2
    :return: distance between points 1 and 2
    """
    distance_point = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5
    return distance_point


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
    discr = b**2 - 4*a*c
    if discr < 0:
        x1, x2 = None, None
    elif discr == 0:
        x1, x2 = -b / (2 * a), -b / (2 * a)
    else:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
    return x1, x2


def is_admin(user: dict) -> bool:
    """
    Gets a user and return if the user is admin or not
    User is a dict, the info about user admin status may be present in fields:
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param user: dictionary with user info
    :return: True or False
    """
    user_is_admin = False
    users = set(user.keys())
    keys = users.intersection({'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'})
    key = list(keys)
    if key:
        print(key)
        return user.get(key[0], False)
    return user_is_admin


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
    miller.249@sgdyyur.com
    """
    rand_string = ''
    for i in range(random.randint(5, 7)):
        rand_string += random.choice(string.ascii_lowercase)
    name = random.choice(names)
    integer = random.randint(100, 999)
    domain = random.choice(domains)
    email = f'{name}.{integer}@{rand_string}.{domain}'
    return email


def find_product(all_products, search_word):
    """
    Create a function to search among products and find by keywords
    :param all_products: iterable of some products
    :param search_word: string to search in product name or product description, case-insensitive
    :return: list of products
    """
    found = []
    search_word = search_word.lower()
    for product in all_products:
        if search_word in (product.get('title')).lower() or search_word in (product.get('description')).lower():
            found.append(product)
        if len(found) == 0:
            found = ['Products not found']
    return found


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
    filename = 'User not found'
    for user in users:
        if search_name.lower() == user['firstName'].lower() or search_name.lower() == user['lastName'].lower():
            first_name = user['firstName']
            last_name = user['lastName']
            filename = open(f'{first_name.title()}_{last_name.title()}.txt', "w")
            filename.write(f"{first_name.title()}_{last_name.title()}")
            filename.close()
            return f'File "{first_name.title()}_{last_name.title()}.txt" was created'
        else:
            return filename


if __name__ == '__main__':
    print('Start')

    # Task 1
    # distance_between_points = distance(12, 211, 11, 64)
    # print(distance_between_points)

    # Task 2
    # quadratic_equation = quadratic_equation(1, 0, 0)
    # print(quadratic_equation)

    # Task 3
    # with open('../lesson_7/users.json') as jsonfile:
    #     data = json.load(jsonfile)
    # users = data.get('users')
    # for user in users:
    #   print(f'user {user.get("firstName")} is admin: {is_admin(user)}')

    # Task 4
    # names = ['andy', 'kali', 'greg', 'fred', 'ben', 'sofie', 'volly', 'metty']
    # domains = ['eu', 'us', 'net', 'org', 'com', 'ua', 'ge', 'kz']
    # e_mail = generate_email(names, domains)
    # print(e_mail)

    # Task 5
    # json_file = 'products.json'
    # search_word = 'phone'
    #
    # with open(json_file) as js:
    #     data = json.load(js)
    # products = data.get('products')
    # found = find_product(products, search_word)
    # for item in found:
    #     print(item)

    # Task 6
    # with open('../lesson_7/users.json') as js:
    #     data = json.load(js)
    # users = data.get('users')
    #
    # txt_file = write_user_to_file(users, 'MEdhuRst')
    # print(txt_file)
