import json
import random
from lesson_9.home_task import is_admin, find_product
from lesson_9.home_task import write_user_to_file
# from lesson_9.solved import is_admin


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
    is_admin_user = is_admin(fake_user)
    print(f' Another User:  {is_admin_user}')


def search_products(products, key):
    found = []
    pass
    return found


def check_product_search():
    with open('products.json') as js:
        data = json.load(js)

    products = data.get('products')

    search_word = 'iphone'
    found1 = find_product(products, search_word)
    print(len(found1), found1)
    found2 = find_product(products, 'glass')
    print(len(found2), found2)
    found3 = find_product(products, 'shield')
    print(len(found3), found3)
    found4 = find_product(products, 'bayraktar')
    print(len(found4), found4)
    found5 = find_product(products, '')
    print(len(found4), found4)


def check_file_write():
    with open('../lesson_7/users.json') as js:
        data = json.load(js)

    users = data.get('users')
    user_found = write_user_to_file(users, search_name='Eleanora')
    print(user_found)       # ELeanora_Shultz.txt

    user_not_found = write_user_to_file(users, search_name='rjfgskjfghk')
    print(user_not_found)       # ''



if __name__ == '__main__':
    # update_users_json()
    check_product_search()
    check_admin()
    check_file_write()
