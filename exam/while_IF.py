# Author: Pascal Walter 4924063
x = input_int()
if x > 42:
    y = 0
    while y < 42:
        y = y + 1
else:
    while x < 42:
        x = x + 1

print(x)

x = 10
while x >= -10:
    if x > 0:
        print(x)
    else:
        print(x * (-1))
    x = x - 1
