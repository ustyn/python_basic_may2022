# Type conversions and variables as a link
from datetime import datetime


# 1.  perform and check. why it works this way??
a = 5
b = a
c = a
a += 1
b = a + 100
#  First try to count what the result of each a, b, c and check yourself with printing them like print(a); print(b) ...
# Was your suggestion correct or not?

# <insert your code HERE, print variables to check, was your suggestion correct or not>

# 1.1 Check yourself with lists
l1 = [1, 2, 3, 4, 5]
l2 = l1
l1.append(6)
l3 = l2
l2.append(7)
l4 = [1, 2, 3, 4, 5, 6]
print(l3 == l1)     # What does it print here and why??
print(l3 is l1)     # What does it print here and why??

print(l4 == l1)     # What does it print here and why??
print(l4 is l1)     # What does it print here and why??


# 2. Try to convert variables and make this part work correct.
# here we are just trying to count the sum of two variables
first = input('Enter the first variable A: ')
second = input('Enter the second variable B: ')

# Fix previous lines (or add new) to make result correct
print(f'Ok, I`ve counted it! A + B = {first + second}.')


# 3. Fix this task
# I want to check if current time is before 12:00 or after
now = datetime.now()
a = now > "12:00"           # UPS. How can we fix it??
# You need to fix previous string.
# First of all, "a" is not a good name for this variable. You need to change this name, so
# it can reflect what the sense of the value it is linked to.
# Second, you have an error here, try to make comparison correct, so it will return True,
# if the current time is later than 12:00, and False otherwise.
# for example, if you perform this task in the morning at 10:45, you will have False.
# But if you like me prefer to work in the evening at 23:45, you will have True.
print(f'Now later than 12:00: {a}, because now {now}')
