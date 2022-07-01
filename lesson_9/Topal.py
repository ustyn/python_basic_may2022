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
        # TODO: can we make complex roots in this case instead of returning str "не існує"
        x1 = "не існує"
        x2 = "не існує"
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
    # Fixme: we dont really need to read users here
    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    is_admin = False
    # insert your code here

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
    random_str = ''.join(random.choice(allowedChars) for _ in range(5, 7))
    email = random.choice(names) + "." + random_number + random_str + "." + random.choice(domains)
    return email


def find_product(all_products, search_word):
    """
    Create a function to search among products and find by keywords
    :param all_products: iterable of some products
    :param search_word: string to search in product name or product description, case-insensitive
    :return: list of products
    """
    # Fixme: we dont really need to read prodyucts here
    with open('products.json') as js:
        data = json.load(js)

    found = []
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
    # Fixme: we dont really need to read users here
    with open('../lesson_7/users.json') as js:
        data = json.load(js)
    pass


if __name__ == '__main__':
    filename = 'users.json'

    # 1
    х1 = 3
    х2 = 5
    y1 = 1
    y2 = 1
    print('distance between points', distance)
    # 2
    a = 1
    b = 2
    c = 3
    print('square equation roots', quadratic_equation)
    # 3
    print(is_admin)
    # 4
    names = ['Afan', 'Andre', 'Grey', 'Fox']
    domains = ["com", "ua", "ru", "net"]
    print('Your email:', generate_email)
    # 5
    print(find_product)
    # 6
    print("Username is :", write_user_to_file)