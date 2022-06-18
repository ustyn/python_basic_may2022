import random
from lesson_3.helper import USERS, HIGH_SPARROW, NO_ONE

uniq_cities = []

counter = 1
inner_counter = 0

all_characters = USERS + [HIGH_SPARROW, NO_ONE]
random.shuffle(all_characters)
l1 = list()

for user in all_characters:
    name = user.get('First name')
    if name == 'Jamie':
        continue
    print('Element #', counter)
    print(name)
    city_from = user.get('From')
    if city_from not in uniq_cities:
        uniq_cities.append(city_from)
    else:
        print('This city already counted', city_from)

    # stop when found Dayeneris
    if name == 'Dayneris':
        break
    print('*' * 20)
    counter += 1

print('inner_counter = ', inner_counter)
print('cities : ', uniq_cities)
print(' ok, end')
