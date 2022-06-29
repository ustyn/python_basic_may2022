import json
import random


def is_admin(user):
    """
    Gets a user and return if the user is admin or not
    User is a dict, the fields of admin status may be present in field :
    'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'
    :param user: dictionary with user info
    :return: True or False
    """
    pass


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


def check_admin():
    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    users = data.get('users')
    for user in users:
        print(f'user {user.get("firstName")} is admin: {is_admin(user)}')


def search_products(products, key):
    found = []
    pass
    return found


def check_product_search():
    with open('products.json') as js:
        data = json.load(js)

    products = data.get('products')

    search_word = 'iphone'
    found1 = search_products(products, search_word)
    print(len(found1), found1)
    found2 = search_products(products, 'glass')
    print(len(found2), found2)
    found3 = search_products(products, 'shield')
    print(len(found3), found3)
    found4 = search_products(products, 'bayraktar')
    print(len(found4), found4)


if __name__ == '__main__':
    # update_users_json()
    check_product_search()