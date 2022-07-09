from math import sqrt
import json
import random


# done
def distance(x1, y1, x2, y2):
    """
    Function get coordinates of two points and returns a distance between them
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """

    dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

# done
def quadratic_equation(a, b, c):
    """
    Return the roots of the quadratic equation
    a * x^2 + b*x + c = 0
    :param a: first argument, couldn't not be 0
    :param b: second argument
    :param c: third argument
    :return: square equation roots
    """
    try:
        assert a != 0
    except AssertionError:
        return 'Error: "a" can`t be 0'

    d = b ** 2 - 4 * a * c

    if d < 0:
        return None

    if d > 0:
        x1 = ((-b - sqrt(d)) / (2 * a))
        x2 = ((-b + sqrt(d)) / (2 * a))
        return x1, x2

# done
def is_admin(user: dict) -> bool:
    """
    Gets a user and return if the user is admin or not
    User is a dict, the info about user admin status may be present in fields:
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param status:
    :param user: dictionary with user info
    :return: True or False
    """

    admin_status = False
    if 'is_admin' in user:
        admin_status = user.get('is_admin')
    elif 'admin' in user:
        admin_status = user.get('admin')
    elif 'super_user' in user:
        admin_status = user.get('super_user')
    elif 'superuser' in user:
        admin_status = user.get('superuser')
    elif 'is_root' in user:
        admin_status = user.get('is_root')
    elif 'root' in user:
        admin_status = user.get('root')

    return admin_status

# done
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

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    mail_service_name = ''
    for x in range(7):
        mail_service_name += random.choice(letters)

    email = f'{random.choice(names)}.{random.choice(range(100, 999))}@{mail_service_name}.{random.choice(domains)}'
    return email

# done
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
    # found = []
    # new_filename = ''
    #
    # for user in users:
    #     if search_name == user['firstName'] or search_name == user['lastName']:
    #         found.append(user)
    #         f_name = user['firstName']
    #         l_name = user['lastName']
    #         new_filename = f'{f_name}_{l_name}'
    #         return f'File "{new_filename}.txt" was created'
    #     else:
    #         return new_filename
    #
    # with open(f'../lesson_9/{new_filename}.txt', 'w') as txt:
    #     for k, v in found[0].items():
    #         txt.write('{}: {}\n'.format(k, v))

    found = []
    new_filename = ''

    for user in users:
        f_name = user['firstName']
        l_name = user['lastName']
        if search_name == f_name or search_name == l_name:
            with open(f'../lesson_9/{f_name}_{l_name}.txt', 'w') as txt:
                for k, v in user.items():
                    txt.write(f'{k}:{v} \n')
            new_filename += f'{f_name}_{l_name}.txt\n'
            found.append(user)

    return new_filename



if __name__ == '__main__':

    task1 = distance(1.5, 3, 2.2, 5)
    print('The distance between  points is calculated by the formula\033[1m AB = √((xb - xa)2 + (yb - ya)2) \033[0m')
    print('Distance =', task1)

    print('')
    print('*' * 25)
    print('')

    # ===================================================

    task2 = quadratic_equation(3, 14, 5)
    print(task2)

    print('')
    print('*' * 25)
    print('')

    # ===================================================

    with open('../lesson_7/users.json') as js:
        data = json.load(js)
    users = data.get('users')

    for user in users:
        task3 = is_admin(user)
        print(f'user {user.get("firstName")} is admin -', task3)

    print('')
    print('*' * 25)
    print('')

    # ===================================================

    names = ['stefania', 'taras', 'kit_stepan']
    domains = ['net', 'com', 'ua']

    task4 = generate_email(names, domains)
    print('Your new beautiful e-mail address:', task4)

    print('')
    print('*' * 25)
    print('')

    # ===================================================
    with open('products.json') as js:
        data = json.load(js)

    products = data.get('products')
    search = 'Apple'
    task5 = find_product(products, search)
    print(f'I searched for a product by the word "{search}" and ... {task5}')

    print('')
    print('*' * 25)
    print('')

    # ===================================================

    task5 = write_user_to_file(users, 'Medhurst')
    print(task5)

