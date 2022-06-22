# https://dummyjson.com/users?limit=50
import sys
import json
import os
from lesson_3.helper import USERS, NO_ONE

# users = USERS

sum = 10000


def args_function(*args, **kwargs):
    '''
    kwargs == key word arguments
    :param args:
    :param kwargs:
    :return:
    '''
    if args:
        print('I got first ', args[0])
        # print('I got b', b)
        print(' I also got args: ', args)
    else:
        print('no params passed inside')
    if kwargs:
        print('WOW, i also got key words arguments:')
        print(kwargs)
        if 'user' in kwargs:
            user = kwargs.get('user')
        else:
            print('NO USER')
            user = None


def filter_db(users, **kwargs):
    """
    Filter some collection( users) nad find user by username
    :param users: users collection
    # :param user_name: user name to search
    :return: element from collection with corresponding user_name or empty dict if not found
    """

    sum = 'summs'
    found = []
    from_ = kwargs.get('from_')
    user_name = kwargs.get('user_name')
    for element in users:
        if user_name and element.get('First name') == user_name:
            found = element
            break
        if from_ and element.get('From') == from_:
            found.append(element)
    return found


def bad_function(list_to_process: list = None, symbol: str = '*', n=5):
    if list_to_process is None:
        list_to_process = []
    list_to_process.extend([symbol] * n)
    return list_to_process


def print_nested_dict(data, indent=''):
    """

    Print nested dict with indentation
    :param data: dictionary to print
    :param indent: indentation, empty string by default
    """

    if isinstance(data, list):
        # good practice to check type of the object
        print(f'{indent}[')
        for item in data:
            print_nested_dict(item, indent=indent + ' ' * 3)
        print(f'{indent}]')
    elif isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, dict):
                print(f'{indent}'+'{')
                print_nested_dict(v, indent=indent + ' ' * 3)
                print(f'{indent}' + '}')
            else:
                print(f'{indent}{k}: {v}')
    else:
        print(data)


def print_json_example():
    print('=' * 77)
    filename = 'lesson_7/users.json'
    users_from_file = json.load(open(filename, 'r'))
    users_to_print = users_from_file.get('users')[:10]
    print_nested_dict(users_to_print)


def count_files(folder, verbose=False):
    """

    :param folder: folder to count files
    :param verbose: flag key word argument, to print or not filenames of found files
    :return:
    """
    counter = 0
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        # watch out this lifehack: to print or not to print in a single line of code
        print(path) if verbose else None
        if os.path.isfile(path):
            counter += 1
        if os.path.isdir(path):
            inner_files = count_files(path, verbose)
            counter += inner_files
    return counter


def count_files_example():
    print('=' * 77)
    folder_name = os.getcwd()
    print("Call count files WITH print filenames:  verbose=True")
    total_files = count_files(folder_name, verbose=True)
    print('Total files: ', total_files)

    print('=' * 77)
    print("Call count files without print: with verbose=False")
    total_files = count_files(folder_name, verbose=False)
    print('Total files: ', total_files)


def args_kwargs_example():
    print('=' * 77)
    print('FIRST CALL: with a, b')
    args_function(1, 2)

    print('=' * 77)
    print('SECOND CALL: with a, b, ...')
    args_function(1, 2, 3, 4, 5)

    print('=' * 77)
    print('THIRD CALL: no arguments')
    args_function()

    print('=' * 77)
    print('4th CALL: with kwargs')
    args_function(10, 20, user='Dmytro', date='22.06.2022')


def filter_function_example():
    print('=' * 77)
    name = 'Aria'
    user = filter_db(USERS, user_name=name)
    print(user)
    print('FROM ', user.get('From'))

    print('=' * 77)
    users_from_WF = filter_db(USERS, from_='Kings Landing')
    for user in users_from_WF:
        print(user)

    found_no = filter_db([], from_='')
    print('found no: ', found_no)
    print('=' * 77)


def bad_function_example():
    # sum = 0
    # LEGB - order to find names:
    #     local
    #       enclosing
    #           global
    #               built-ins
    print('this is sum: ', sum)

    l1 = bad_function([1, 2, 3], symbol='$', n=2)
    print(l1)

    l2 = bad_function()
    print(l2)

    l3 = bad_function([1, 2, 23], symbol="5", n=5)
    print(l3)


if __name__ == '__main__':
    print("-- == START == --")

    bad_function_example()

    args_kwargs_example()

    filter_function_example()

    # RECURSIVE function example # 1
    # get users from json and print them all
    print_json_example()

    # RECURSIVE function example # 2
    # count number of files in some folder, including nested folders
    count_files_example()

    print('=' * 77)
    print("-- == END == --")
