# Author: Pascal Walter 4924063
x = input_int()
y = input_int()
z = x % 7 < y % 11
if z:
    print(42)
else:
    print(0)
