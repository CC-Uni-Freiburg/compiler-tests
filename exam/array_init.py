# Author: Pascal Walter 4924063
def ret42() -> int:
    return 42


x = [2 * 2, 4 // 2, 8 % 7, 9 + 9, 8 - 9, -10]

y = [True if x[0] > 0 else False, True and x[2] < 0, False, 4 >= 0, not True]

z = [ret42(), ret42(), ret42(), len(x), len((4,))]

print(x[0] * x[1])
print(42 if y[0] or y[1] else 0)
print(z[0])
