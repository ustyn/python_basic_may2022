# As usual very beginning starts with hello world
print('Hello World!')

name = 'Dmytro Ustynov'
print('1. My name is: ', name)

# here we start with formatting string
name = 'Oleh'
print('2. My name is: {}'.format(name))

name = 'Tatiana'
name2 = 'Olha'

# new version of string formatting starting with Python >3.6
print(f'3. My name is: {name}.  And my daughter`s name is {name2}. ')
# We even can multiply string  like so:
print('*' * 55)

print(f'20 days in seconds is: {20 * 24 * 60 * 60}.')
print(f'30 days in seconds is: {30 * 24 * 60 * 60}.')
print(f'50 days in seconds is: {50 * 24 * 60 * 60}.')

first_name = 'Olha'
last_name = 'Kurkina'

print(f'4. User name: {first_name} {last_name}')
print(f'5. User name: {first_name + " " + last_name}', end='\n\n')      # \n - is row ending, new line
print('6. User name:' ,  first_name,  last_name, 356, sep='___')        # sep - is separator

# how to check documentation for some function: use __doc__ or hover mouse over the function name in few seconds in IDE
print(print.__doc__)

# use shortcut Cntrl+B  to see the function declaration outside your file and explore it
count_me = sum([1, 2, 4, 5])
print(count_me)

# Create multi rows strings with triple quotes("): """
some_text = """Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream."""

result = some_text.split(' ')       # one of the possible functions for text - split text by space symbol " ".
                                    # split() returns a list as a result

print(result)
# another function possible for text - check if the string starts or ends with
print(some_text.startswith('Prints'))
print(some_text.endswith('stream.'))

#  print all functions that I can use with string type:
print(dir(some_text)[::-1])

#  By the way, some_list[::-1] is a lifehack how to reverse list



# numbers
a = 1
b = 25      # integer
c = 3.45    # float
cmplx = complex(1, 3)  # complex number, if you really need it

print(cmplx)

# math functions
a = 1
b = a + 3
d = b * 5
big_number = 100000000000000000000000
print(big_number * 234524365234723)
d = 12 + 35 + (156 - 134878) * 124124
print(d)


# ** power 2**5 = 32, 10**5 = 100000
pow = 10 ** 5
print(pow)

# Different types of division
# simple
print("17 / 6 =", 17 / 6)   # = 2.8333333333333335
# get integer
print(17 // 6)          # 17 // 6 = 2 , because .8333333333333335 was ignored
#  get what left after division
print(17 % 6)               # 17 - (2*6) = 5


# variables
# Name variable as you want except reserved words,
# this will be an ERROR, because 'import' is a reserved word:
# import = 4

# naming convention
number_of_days_passed = 10      # snakecase. preferable
numberOfDaysPassed = 10         # camelcase. still possible


# Possible names but they are built in functions. DO NOT use as variable names
# min(1)
# sum(34)
# sorted()
# id(2323)
# hash()
# abs()
# len()
print ('-END-')
print('*' * 55)
