import random
from datetime import datetime

USERS = [
    {'First name': 'Eddard',
     'Last name': 'Stark',
     'From': 'Winterfell'},
    {'First name': 'Rob',
     'Last name': 'Stark',
     'From': 'Winterfell'},
    {'First name': 'Aria',
     'Last name': 'Stark',
     'From': 'Winterfell'},
    {'First name': 'John',
     'Last name': 'Snow',
     'From': 'Winterfell'},
    {'First name': 'Jamie',
     'Last name': 'Lannister',
     'From': 'Casterly Rock'},
    {'First name': 'Cercei',
     'Last name': 'Lannister',
     'From': 'Casterly Rock'},
    {'First name': 'Tirion',
     'Last name': 'Lannister',
     'Nickname': 'Dwarf',
     'From': 'Casterly Rock'},
    {'First name': 'Jofrey',
     'Last name': 'Barateon',
     'From': 'Kings Landing'},
    {'First name': 'Dayneris',
     'Last name': 'Targarien',
     'Status': 'Stormborn  & Dragon`s Mother',
     'From': 'Dragon Stone'},
    {'First name': 'Sandor',
     'Last name': 'Kligan',
     'Nickname': 'Hound',
     'From': None},
]

HIGH_SPARROW = {'First name': 'High Sparrow',
                'Last name': None,
                'Religion': 'Seven`s',
                'From': 'Kings Landing'}

NO_ONE = {'First name': None,
          'Last name': None,
          'Nickname': 'No One',
          'From': 'Braavos'}

CONFIG = {'db_name': 'thrones_db',
          'host': 'amazon://aws.2345-3456-7890.bbllaa',
          'destination': 'production',
          'port': 1001,
          'max_users': 50,
          'secret_key': 'eyd38gruy$&FGgergi43094509@VY$',
          'user': 'Dmytro',
          'password': 1234,
          # 'debug': True,
          'working_time_start': datetime.now(),
          'working_time_end': datetime.now(),
          'allowed_users_ids': [5, 6, 7],
          'allowed_formats': tuple({'mp3', 'wav', 'm4a', 'flac'})
          }

RANDOM_NUMBERS = [random.randint(1, 10000) for _ in range(1000)]
