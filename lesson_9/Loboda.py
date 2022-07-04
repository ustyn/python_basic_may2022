import math
import json
import random
import string

def distance(x1, y1, x2, y2):
    """
    Function get coordinates of two points and returns a distance between them
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    point_A = [x1, y1]
    point_B = [x2, y2]
    distance_AB = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return distance_AB


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
    D = (b**2 - 4*a*c)
    if D > 0:
        x1 = ((-b) + math.sqrt(D))/(2*a)
        x2 = ((-b) - math.sqrt(D))/(2*a)
    elif D == 0:
        x1 = (-b)/(2*a)
        x2 = 'one root'
    else:
        x1 = "no roots"
        x2 = None
    return x1, x2



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
    for itemA in user:
        for itemB in list_admin_name:
            if itemA == itemB:
                    is_admin = user.get(itemA)
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
    # name = random.choice(names)
    # domain = random.choice(domains)
    # number = random.randint(100, 999)
    letter_code = ''
    for i in range(random.randint(5, 7)):
        letter_code += random.choice(string.ascii_lowercase)
    email = f'{random.choice(names)}.{random.randint(100, 999)}@{letter_code}.{random.choice(domains)}'
    return email


def find_product(all_products, search_word):
    """
    Create a function to search among products and find by keywords
    :param all_products: iterable of some products
    :param search_word: string to search in product name or product description, case-insensitive
    :return: list of products
    """
    search_word = search_word.lower()
    found = []
    for item in all_products:
        for k in item.values():
            if type(k) == type(search_word):
                k = k.lower()
                if search_word in k:
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
        FirstName = (item.get('firstName')).lower()
        Lastname = (item.get('lastName')).lower()
        if search_name == FirstName or search_name == Lastname:
            with open(f'{FirstName.title()}_{Lastname.title()}.txt', 'w', encoding="utf-8") as file_txt:
                for key, val in item.items():
                    file_txt.write(f'{key}:{val}\n')
            found += f'{FirstName.title()}_{Lastname.title()}.txt\n'
    return found

if __name__ == '__main__':
    print('Ok, started!')

    # dist_point = distance(x1=10, y1=20, x2=30, y2=40)                       #1
    # print(dist_point)

    # QUADRATIC_EQ = quadratic_equation(a=2, b=5, c=-3)                        #2
    # print(QUADRATIC_EQ)

    # with open('../lesson_7/users.json') as js:                              #3
    #     data = json.load(js)
    # users = data.get('users')
    # user = random.choice(users)
    # print(f'user {user.get("firstName")} is admin: {is_admin(user)}')


    # names = ['jonhns', 'darko', 'stiller', 'wayne', 'adams']                 #4
    # domains = ['com', 'ua', 'net', 'org']
    # e_mail = generate_email(names, domains)
    # print(e_mail)


    # with open('products.json') as js:                                          #5
    #     data = json.load(js)
    # products = data.get('products')
    # search_word = 'Perfume'
    # found = find_product(products, search_word)
    # print(len(found), found)


    # with open('../lesson_7/users.json') as js:                                  #6
    #     data = json.load(js)
    # users = data.get('users')
    # user_found = write_user_to_file(users, search_name='LENNA')
    # print(user_found)