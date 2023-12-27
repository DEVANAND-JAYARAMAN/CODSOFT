import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

b=int(input("Enter the desired length of the password: "))
print(generate_password(b))  # Generates according to user desired length character password