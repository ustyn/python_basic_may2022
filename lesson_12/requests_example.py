import json
import requests

URL_TEMPLATE = 'https://dummyjson.com/users?limit={}'


def get_users_json(number=50):
    url = URL_TEMPLATE.format(number)

    result = requests.get(url)

    data = result.json()
    return data


def ping_lms():
    url = 'https://lms.ithillel.ua/'

    data = requests.get(url)
    print('got data')


if __name__ == '__main__':
    print('START')
    ping_lms()
    all_users = get_users_json(100)

    with open('all_users.json', 'w') as js_file:
        json.dump(all_users, js_file)

    print('DOWNLOADED SUCCESSFULLY')