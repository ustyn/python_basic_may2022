import math
import json
import random

# def distance(x1, y1, x2, y2):
#     """
#     Function get coordinates of two points and returns a distance between them
#     :param x1:
#     :param y1:
#     :param x2:
#     :param y2:
#     :return:
#     """
#     point_A = [x1, y1]
#     point_B = [x2, y2]
#     distance_ = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
#     return distance_


# def quadratic_equation(a, b, c):
#     """
#     Return the roots of the quadratic equation
#     a * x^2 + b*x + c = 0
#     :param a: first argument, couldn't not be 0
#     :param b: second argument
#     :param c: third argument
#     :return: square equation roots
#     """
#     assert a != 0
#     x1, x2 = None, None
#     D = (b**2 - 4*a*c)
#     if D > 0:
#         x1 = ((-b) + math.sqrt(D))/(2*a)
#         x2 = ((-b) - math.sqrt(D))/(2*a)
#     elif D == 0:
#         x1 = (-b)/(2*a)
#         x2 = 'one root'
#     else:
#         x1 = "no roots"
#         x2 = None
#     return x1, x2



def is_admin(user: dict) -> bool:
    """
    Gets a user and return if the user is admin or not
    User is a dict, the info about user admin status may be present in fields:
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param user: dictionary with user info
    :return: True or False
    """

    is_admin = False
    list_admin_name = ['is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root']
    is_admin = False
    for itemA in user:
        for itemB in list_admin_name:
            if itemA == itemB:
                    is_admin = user.get(itemA)
    return is_admin



# def generate_email(names, domains):
#     """
#     Даны списки names и domains (создать самостоятельно).
#     Написать функцию для генерирования e-mail в формате:
#     фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
#     фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
#     Строку и число генерировать случайным образом.
#
#     Пример использования функции:
#     names = ["king", "miller", "kean"]
#     domains = ["net", "com", "ua"]
#     e_mail = create_email(domains, names)
#     print(e_mail)
#     >>>miller.249@sgdyyur.com
#     """
#     email = ''
#     return email


# def find_product(all_products, search_word):
#     """
#     Create a function to search among products and find by keywords
#     :param all_products: iterable of some products
#     :param search_word: string to search in product name or product description, case-insensitive
#     :return: list of products
#     """
#     found = []
#     return found


# def write_user_to_file(users, search_name):
#     """
#     Write a function, that takes a user_name or last name find the user and write the result
#     to a file <FirstName_LastName>.txt
#     The user data inside should be written in a pretty format:
#
#     Key     :       Value
#     :param users: iterable of users
#     :param search_name: First or Last name of the user to search, case insensitive
#     :return:  str file_name of the user if found or empty string if not
#     """
#     pass


if __name__ == '__main__':
    # print('Ok, started!')

    # dist_point = distance(x1=10, y1=20, x2=30, y2=40)                   #1
    # print(dist_point)

    # QUADRATIC = quadratic_equation(a=2, b=5, c=3)                       #2
    # print(QUADRATIC)

    with open('../lesson_7/users.json') as js:                            #3
        data = json.load(js)
    users = data.get('users')
    user = random.choice(users)
    print(f'user {user.get("firstName")} is admin: {is_admin(user)}')

