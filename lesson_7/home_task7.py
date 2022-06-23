import json


def find_youngest_user(users, **kwargs):
    """
    Find the yongest user among all users
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
    Find the oldest user among all users
    :param users: list of users to find
    :param name: name of the user to find
    :return: dictionary with the oldest user
    """
    found = []
    # insert your code here to implement
    return found


if __name__ == '__main__':

    filename = 'users.json'
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)

    # place the red dot (stop debug) and fix the code to take correct users
    json_users = data.users

    # 1. Find the youngest user
    youngest = find_youngest_user(json_users)
    print('The youngest user is: \n', youngest)

    # 2. find the oldest user
    oldest = find_oldest_user(json_users)
    print('The oldest user is: \n', oldest)

    # 3. find users by name:
    name = 'some user name to find'
    found = find_by_name(json_users, name)
    print('I`ve found user by his name:')
