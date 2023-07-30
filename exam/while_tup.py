# Author: Pascal Walter 4924063
x = (1, 2, 3, 42)
y = 10
while x[0] - y < 0:
    y = y - 1
    z = x[0] + (1, 2)[1]
print(x[3])

y = 10
while (4, 2)[0] - y < len(x):
    y = y - 2
print(x[3])
