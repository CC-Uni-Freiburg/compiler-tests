# Author: Pascal Walter 4924063
x = [0, 42, 1, 42]
if len(x) == 4:
    print(42)

if x[0] > -1:
    print(42)
else:
    print(100)

if [1, 2, 3][2 * 3 - 4] > 2:
    print(42)
else:
    print(100)


print(x[1] if x[1 + 0] == 42 else 0)
print(x[2 + 1] if len([[1, 2, 3], [4, 5, 6]][0 + 0]) > 0 else 0)
