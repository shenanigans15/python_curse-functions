import string
import random


def password_generator(longitud):

    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(longitud):
        password += random.choice(caracteres)
    return password


print(password_generator(25))
