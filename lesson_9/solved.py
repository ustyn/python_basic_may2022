"""
here the examples how I have solved some tasks

"""

def is_admin(user):
    key = list(set(user.keys()).intersection(
        {'is_admin', 'admin', 'super_user', 'superuser', 'is_root', 'root'})
    )
    if key:
        print(key)
        return user.get(key[0], False)
    return False


def quadratic_equation(a, b, c):
    """
    Return the roots of the quadratic equation
    a * x^2 + b*x + c = 0
    :param a: first argument, couldn't not be 0
    :param b: second argument
    :param c: third argument
    :return: square equation roots
    """
    assert a != 0
    # x1, x2 = None, None
    discriminant = (b**2 - 4 * a * c)
    # print(discriminant)
    if discriminant < 0:
        # D < 0 --> complex roots
        x1 = complex(-b / (2 * a), ((-1 * discriminant)**0.5) / (2*a))
        x2 = complex(-b / (2 * a), -1 * ((-1 * discriminant)**0.5) / (2*a))
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
    return x1, x2


def not_perfect_quadratic(a,b,c):
    """"
    why this function is not so good?
    it looses the case with D=0
    """
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
    else:
        x1, x2 = None, None
    # but what if D will be 0 ??
    return x1, x2



