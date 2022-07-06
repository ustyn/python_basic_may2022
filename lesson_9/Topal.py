import json
import os
import sys
import math
import random
import string

def distance(x1, y1, x2, y2):
    """
    Function get coordinates of two points and returns a distance between them
    :param x1: Координата по х первой точки
    :param y1: Координата по у первой точки
    :param x2: Координата по х второй точки
    :param y2: Координата по у второй точки
    :return: Расстояние между точками
    """
    AС = x2 - x1
    BC = y2 - y1
    АB = (AС ** 2 + BC ** 2) ** 0.5
    return АB


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
    x1, x2 = None, None
    # insert your code here
    D = b ** 2 - 4 * a * c
    if D < 0:
        x1 = "не існує"
        x2 = "не існуе"
    else:
        if D == 0:
            x1 = (-b + D ** 0.5) / 2 * a
            x2 = (-b - D ** 0.5) / 2 * a
        else:
            x1 = (-b + D ** 0.5) / 2 * a
            x2 = (-b - D ** 0.5) / 2 * a

    return x1, x2


def is_admin(user: dict) -> bool:
    """
    Gets a user and return if the user is admin or not
    User is a dict, the info about user admin status may be present in fields:
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param user: dictionary with user info
    :return: True or False
    """
    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    is_admin = False
    # insert your code here
    names_admin = ['is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root']
    for i in user:
        for a in names_admin:
            if i == a:
                is_admin = user.get(i)

    return is_admin


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
    >>>miller.249@sgdyyur.com
    """
    email = ''
    from random import randint
    random_number = str(randint(100, 999))
    allowedChars = string.ascii_letters
    random_str = ''.join(random.choice(allowedChars).lower() for _ in range(1, 8))
    email = random.choice(names) + "." + random_number + random_str + "." + random.choice(domains)
    return email


def find_product(all_products, search_word):
    """
    Create a function to search among products and find by keywords
    :param all_products: iterable of some products
    :param search_word: string to search in product name or product description, case-insensitive
    :return: list of products
    """

    found = []
    for item in all_products:
        products_name = (item.get('title'))
        description_product = (item.get('description'))
        if search_word in products_name or description_product:
            found.append(item)
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
    found = ''
    search_name = search_name.lower()
    for item in users:
        Firstname = (item.get('firstName')).lower()
        Lastname = (item.get('lastName')).lower()
        if search_name == Firstname or search_name == Lastname:
            with open(f'{Firstname.title()}_{Lastname.title()}.txt', 'w', encoding="utf-8") as file_txt:
                for k, v in item.items():
                    file_txt.write(f'{k}:{v}')
            found += f'{Firstname.title()}_{Lastname.title()}.txt ; '
    return found

    pass

if __name__ == '__main__':
    filename = 'users.json'

    # 1
    print("Функция 1")
    # х1 = 3
    # х2 = 5
    # y1 = 1
    # y2 = 1
    distance_new = distance(x1=3, x2=5, y1=1, y2=1)
    print('distance between points = ', distance_new)
    # 2
    print("Функция 2")
    # a = 1
    # b = 2
    # c = 3
    quadratic_equation_new = quadratic_equation(a=2, b=15, c=3)
    print('Корни квадратного уравнения:', quadratic_equation_new)
    # 3
    print("Функция 3")
    with open('../lesson_7/users.json') as js:
        data = json.load(js)
    users = data.get('users')
    user = random.choice(users)
    print(f'Пользователь {user.get("firstName")} админ = {is_admin(user)}')
    # 4
    print("Функция 4")
    names = ['Afan', 'Andre', 'Grey', 'Fox']
    domains = ["com", "ua", "ru", "net"]
    generate_email_new = generate_email(names, domains)
    print('Ваш адрес:', generate_email_new)
    # 5
    print("Функция 5")
    with open('products.json') as js:
        data = json.load(js)
    products = data.get('products')
    search_word = 'watch'
    found_product_new = find_product(products, search_word)
    print(found_product_new)
    # 6
    print("Функция 6")
    with open('../lesson_7/users.json') as js:
        data = json.load(js)
    users = data.get('users')
    user_found = write_user_to_file(users, search_name='Terry')
    print("Username is :", user_found)