import json


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


def is_admin(user: dict) -> bool:
    """
    Gets a user and return if the user is admin or not
    User is a dict, the info about user admin status may be present in fields:
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param user: dictionary with user info
    :return: True or False
    """
    is_admin = False
    # insert your code here
    if user.get('is_admin') == True or user.get('admin') == True or user.get('super_user') == True or user.get(
            'superuser') == True or user.get('is_root') == True or user.get('root') == True:
        is_admin = True
    else:
        is_admin = False
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

    return email

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
