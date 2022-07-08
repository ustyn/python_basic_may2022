import json
import random
from lesson_9.home_task import find_product_v2
from lesson_9.Loboda import is_admin, find_product
from lesson_9.Loboda import write_user_to_file
from lesson_9.Loboda import distance
from lesson_9.Loboda import quadratic_equation


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
    fake_user = {"username": "Adam", "super_user": True}

    print(f' Another User:  {is_admin(fake_user)}')


def find_product(all_products, search_word):
    """
    Create a function to search among products and find by keywords
    :param all_products: iterable of some products
    :param search_word: string to search in product name or product description, case-insensitive
    :return: list of products
    """
    found = []
    for product in all_products:
        descr = product.get('description', '').lower()
        title = product.get('title', '').lower()
        if search_word.lower() in descr or search_word.lower() in title:
            found.append(product)
    return found


def check_product_search():
    with open('products.json') as js:
        data = json.load(js)

    products = data.get('products')

    search_word = 'iphone'
    found1 = find_product(products, search_word)
    print('iphone: ', len(found1), found1)
    found2 = find_product(products, 'glass')
    print('glass: ', len(found2), found2)

    found2 = find_product(products, 'sunglasses')
    print('sunglasses: ', len(found2), found2)

    found3 = find_product(products, 'shield')
    print('shield: ', len(found3), found3)
    found4 = find_product(products, 'bayraktar')
    print('not found: ', len(found4), found4)
    found5 = find_product(products, '')
    print(len(found4), found4)

    is_found, _ = find_product_v2(products, 'sunglasses')


def check_file_write():
    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    users = data.get('users')
    user_found = write_user_to_file(users, search_name='Eleanora')
    print(user_found)       # ELeanora_Shultz.txt

    user_not_found = write_user_to_file(users, search_name='rjfgskjfghk')
    print(user_not_found)       # ''


def check_quadratic():
    x1, x2 = quadratic_equation(1, 12, -13)
    print(x1, x2)

    x1, x2 = quadratic_equation(1, -5, 6)
    print(x1, x2)

    x1, x2 = quadratic_equation(1, -3, 8.5)
    print(x1, x2)

    x1, x2 = quadratic_equation(1, 0, 0)
    print(x1, x2)


def check_distance():
    print('distance 1 ', distance(0, 0, 3, 4))  # 5
    print('distance 2 ', distance(-1, 0, 1, 0))  # 2
    print('distance 3 ', distance(-10, 0, 3, 5))  # 13.92838827718412


if __name__ == '__main__':
    # update_users_json()
    check_product_search()
    check_admin()
    check_distance()
    check_file_write()
    check_quadratic()
