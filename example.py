import fasht
import random

keys = ['hello', 'world', 'good', 'fegeya', 'algorithm', 'fast', 'hash', 'lol']

key = f'{keys[0]} {keys[random.randint(1, len(keys) - 1)]}'
print(key, '->', fasht.h(key))