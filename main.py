import random

sogl = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
glas = 'aeyuioAEYUIO'
numbers = '1234567890'
symbols = '=+-@#'
lenght = 12
password = ''
for i in range(random.randint(3, 4)):
    password += random.choice(sogl) + random.choice(glas)

for i in range(random.randint(2, 3)):
    password += random.choice(numbers)

for i in range(random.randint(2, 3)):
    password += random.choice(symbols)
print(password)
