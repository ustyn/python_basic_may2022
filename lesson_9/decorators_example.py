from time import time, sleep
import json
import random


def timer_func(some_function):
    def wrapper(*args, **kwargs):
        t0 = time()
        result = some_function(*args, **kwargs)         # here we perform the function call with args and kwargs
        sleep(random.random())
        print(f'Function "{some_function.__name__}" took: {time() - t0} sec')
        return result
    return wrapper


@timer_func
def find_youngest_user(users, **kwargs):
    """
    Find the yongest user among all users
    :param users: list of users to find
    :param kwargs: may be optional
    :return: dictionary with the youngest user
    """
    found = None
    ages_all = []
    for item in json_users:
        found_age = item.get('age')
        ages_all.append(found_age)
    age_min = min(ages_all)
    for item in json_users:
        # sleep(random.random())
        if item.get('age') == age_min:
            found = item
    return found


@timer_func
def find_oldest_user(users):
    """
    Find the oldest user among all users
    :param users: list of users to find
    :return: dictionary with the oldest user
    """
    found = None
    ages_all = []
    for item in json_users:
        found_age = item.get('age')
        ages_all.append(found_age)
    age_max = max(ages_all)
    for item in json_users:
        if item.get('age') == age_max:
            found = item
    return found


@timer_func
def find_by_name(users, name):
    """
    Find the oldest user among all users
    :param users: list of users to find
    :param name: name of the user to find
    :return: the list of found users or empty list if no users were found
    """
    found = []
    for item in json_users:
        if item.get('firstName') == name:
            found.append(item)
    return found


def example1(arg1=''):
    print('i am function example1')
    print('i got argument arg1 = ', arg1)
    return arg1.upper()


def main():
    s1 = 'eeeee'
    a = print(s1)               # print() returns nothing, so a will be None
    print(a)
    ah = example1('hello world')
    result = example1('eee')
    print(result)
    print(ah)
    # =========
    f1 = example1       # f1 is a function, not the result of the function
    print(f1)
    try:
        f2 = example1()
        print(f2)
    except Exception as e:
        print('f2 exception', str(e))
    try:
        f3 = example1(1, 2, 3)      #   exception with not expected arguments
    except Exception as e:
        print('f3 exception', str(e))
    f1("hello world")


if __name__ == '__main__':

    filename = '../lesson_7/users.json'
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)

    json_users = data.get('users')

    # 1. Find the youngest user
    youngest = find_youngest_user(json_users)
    print('The youngest user is: \n', youngest)

    # 2. find the oldest user
    oldest = find_oldest_user(json_users)
    print('The oldest user is: \n', oldest)

    # 3. find users by name:
    name = 'Eleanora'
    found = find_by_name(json_users, name)
    print(f'I`ve found {len(found)} user by his name: \n')
    for f in found:
        print(f)
    print('==' * 23)
    found_oldest = find_oldest_user(json_users)
    print(found_oldest)
