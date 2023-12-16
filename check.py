import string
import random

letters = string.ascii_uppercase
random_string = ''.join(random.choice(letters) for i in range(6))

print(random_string)