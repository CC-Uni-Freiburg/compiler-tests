# Author: Pascal Walter 4924063
x = ([0, 1], [2, 3])
x[0][0] = 42
print(x[0][2-2])
y = [(42,)]
print(y[0][0])
z = [((1,), (42,))][0][1][0]
print(z)
