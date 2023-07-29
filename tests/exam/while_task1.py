# Author: Pascal Walter 4924063
x = 10
while (((x * 2) // 2) % 100) != 1:
    x = x * 2
    x = x // 4
    x = x % 100
print(x * 42)
