import json
import string
import random


def distance(x1, y1, x2, y2):
    """
    Function get coordinates of two points and returns a distance between them
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return dist


def quadratic_equation(a, b, c):
    """
    Return the roots of the quadratic equation
    a * x^2 + b*x + c = 0
    :param a: first argument, couldn't be 0
    :param b: second argument
    :param c: third argument
    :return: square equation roots
    """
    assert a != 0
    x1, x2 = None, None
    d = 0
    # insert your code here
    d = b ** 2 - 4 * a * c
    if d < 0:
        x1, x2 = None, None
    elif d == 0:
        x1 = (- b + d ** 0.5) / 2 * a
        x2 = x1
    else:
        x1 = (- b + d ** 0.5) / 2 * a
        x2 = (- b - d ** 0.5) / 2 * a
    return x1, x2


def is_admin(user: dict) -> bool:
    """
    Gets a user and return if the user is admin or not
    User is a dict, the info about user admin status may be present in fields:
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param user: dictionary with user info
    :return: True or False
    """
    admin = False
    # insert your code here
    if user.get('is_admin') is True or user.get('admin') is True or user.get('super_user') is True or user.get(
            'superuser') is True or user.get('is_root') is True or user.get('root') is True:
        admin = True
    else:
        admin = False
    return admin

#Teacher's code:
    #key = list(set(user.keys()).intersection({'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'}))
    #intersection = пересічення
    # if key:  #means list key is not empty
    #     print(key)
    #     return user.get(key[0], False)
    # return False


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
    random_letters = ''
    for i in range(random.randint(5, 7)):
        random_letters += random.choice(string.ascii_lowercase)
    email = f'{random.choice(names)}.{str(random.randint(100, 999))}@{random_letters}.{random.choice(domains)}'
    return email


def find_product(all_products, search_word):
    """
    Create a function to search among products and find by keywords
    :param all_products: iterable of some products
    :param search_word: string to search in product name or product description, case-insensitive
    :return: list of products
    """
    found = []
    for product in all_products:
        description = product.get('description')
        title = product.get('title')
        if search_word.lower() in description.lower() or search_word.lower() in title.lower():
            found.append(product)
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
    for user in users:
        if search_name in user.get('firstName') or search_name in user.get('lastName'):
            file_name = f"{user.get('firstName')}_{user.get('lastName')}.txt"
            with open(file_name, 'w') as file:
                for key, value in user.items():
                    user_dict = str(key) + " : " + str(value) + "\n"
                    file.write(user_dict)


def update_users_json():
    """
    Helper function to randomly make some of our users admins
    :return:
    """
    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    users = data.get('users')
    counter = 0
    for item in users:
        is_admin = random.random() > 0.8
        if is_admin:
            key = random.choice(['is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'])
            item[key] = True if random.random() > 0.2 else False
            print(f'Adding admin key {key} for user {item.get("firstName")}')
            counter += 1
    data['users'] = users
    with open('../lesson_7/users.json', 'w') as js_write:
        json.dump(data, js_write)
    print(f'Updated {counter} users')


if __name__ == '__main__':

    # 1. Distance between 2 points
    xa = int(input('Input coordinates: x1 = '))
    ya = int(input('y1 = '))
    xb = int(input('x2 = '))
    yb = int(input('y2 = '))
    distance = distance(xa, ya, xb, yb)
    print(f'Distance between points ({xa},{ya}) and ({xb},{yb}) is {distance}')

    # 2. Roots of a quadratic equation
    a = int(input('Input param a (not 0!): '))
    b = int(input('Input param b: '))
    c = int(input('Input param c: '))
    roots = quadratic_equation(a, b, c)
    if roots is None:
        print('There are no roots for your equation')
    else:
        print(f'Roots for your equation is {roots}')

    # 3. Check if user is admin
    update_users_json()
    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    users = data.get('users')
    for user in users:
        print(f'user {user.get("firstName")} is admin: {is_admin(user)}')

    #4. Generate new email
    names = ['Jenny', 'Mike', 'Alise', 'Daniel', 'Mary', 'Jason']
    domains = ['com', 'net', 'ua', 'uk', 'pl']
    new_email = generate_email(names, domains)
    print(new_email)

    #5. Find product
    with open('products.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        all_products = data.get('products')

    search_word = input('What product do you want to find? ')
    found = find_product(all_products, search_word)
    print(len(found), found)

    #6. Find user and write info in the file
    with open('../lesson_7/users.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        users = data.get('users')

    write_user_to_file(users, 'Terry')
