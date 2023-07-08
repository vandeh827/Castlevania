import random

print("your password: ")

chars = 'ustiejivandeorb225sd'

password = ''

for x in range(5):
    password += random.choice(chars)

print(password)
