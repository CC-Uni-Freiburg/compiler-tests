# Author: Pascal Walter 4924063
x = 2
while (x > 0) and (True):
    z = 42 if True or False else 0
    print(z)
    x = x - 1

while x < 2 or x < 1:
    z = 0 if True and False else 42
    print(z)
    x = x + 1
