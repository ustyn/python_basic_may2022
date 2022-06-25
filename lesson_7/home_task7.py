import datetime
import json
import os
import pickle
import random


def find_youngest_user(users, **kwargs):
    """
    Find the youngest user among all users
    :param users: list of users to find
    :param kwargs: may be optional
    :return: dictionary with the youngest user
    """
    found = None
    # insert your code here to implement
    return found


def find_oldest_user(users):
    """
    Find the oldest user among all users
    :param users: list of users to find
    :return: dictionary with the oldest user
    """
    found = None
    # insert your code here to implement
    return found


def find_by_name(users, name):
    """
    Find the user among all users by his name
    :param users: list of users to find
    :param name: name of the user to find
    :return: the list of found users or empty list if no users were found
    """
    found = []
    # insert your code here to implement
    return found


def serialize_with_pkl(users):
    print(type(users))
    users['my newkey'] = datetime.datetime.now()

    with open('users.json', 'r') as jsonfile:
        data = json.load(jsonfile)

    users['all_data'] = data
    # users['jsonfile'] = jsonfile

    with open('data.pkl', 'wb') as pkl:
        pickle.dump(users, pkl)
    print('OK, ')


def example_with_some_file_to_append(message):
    filename = os.path.join(os.getcwd(), '../data/logs/some_log.log')

    print(os.path.abspath(filename))
    now = datetime.datetime.now()
    data_string = f'{now.strftime("%H:%M:%S")} {message}\n'
    with open(filename, 'a') as file:           # mode 'a' means append
        file.write(data_string)


def examples():
    some_list = [random.randint(-50000, 50000) for _ in range(1000)]
    min_el = min(some_list)
    max_el = max(some_list)
    print(min_el)
    print(max_el)
    found_min = None
    for item in some_list:
        if item < found_min:
            found_min = item
    print('i found min: ', found_min)

    sum_items = 0
    for item in some_list:
        sum_items += item
    print('i summed all: ', sum_items)


if __name__ == '__main__':

    filename = 'users.json'
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)

    # place the red dot (stop debug) and fix the code to take correct users
    json_users = data.get('users')

    # 1. Find the youngest user
    youngest = find_youngest_user(json_users)
    print('The youngest user is: \n', youngest)

    # 2. find the oldest user
    oldest = find_oldest_user(json_users)
    print('The oldest user is: \n', oldest)

    # 3. find users by name:
    name = 'some user name to find'
    found = find_by_name(json_users, name)
    print('I`ve found user by his name: \n', found)
    #
    # serialize_with_pkl(data)
    #
    # example_with_some_file_to_append('Hello world')
    # example_with_some_file_to_append('stop with it')

    examples()
