from lesson_3.helper import USERS, HIGH_SPARROW, NO_ONE

# 1. We import 3 objects from another file, try to inspect them with Cntrl + B / Cmd + B
#   and better understand how to make a correct structure

# 2. Create the list of all characters by merging (appending, extending)
# all elements together from USERS, HIGH_SPARROW and NO_ONE

all_characters = []             # Fixme: this list should contain all characters together.
# random.shuffle(all_characters)
assert len(all_characters) == 12,  \
    "Looks like you still have not joined all 'characters' to a single list. " \
    "Try to make the list with any methods we know."

# 3. Watch the video and repeat - create the unique list with all cities, where our characters from.
cities = 'some collection?'     # Fixme: this collection should contain only unique cities.

# 4. Drop None from cities collection.
#                             Because None is not the city name.
#                             You may drop it here,
#                             Or get additional 10 points,
#                             if you find the way to make it in a single line in p3
#                             by adding a condition.

assert None not in cities, \
    "May be you forget to exclude None from cities name, because 'None' is not the city"
assert len(cities) == 5, \
    "You should have the correct expression"

print(cities)
print('--== THE END ==--')
