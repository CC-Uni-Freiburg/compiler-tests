def sum_up(
    x1: int,
    x2: int,
    x3: int,
    x4: int,
    x5: int,
    x6: int,
    x7: int,
    x8: int,
    x9: int,
    x10: int,
) -> int:
    return x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + 0


def cond(y: int) -> bool:
    return True if (y > 100 and y // 100 <= 3) else False


y = 0
x = 1
while (not cond(y)) and (not cond(sum_up(x, x, x, x, x, x, x, x, x, x))):
    y = sum_up(x, x, x, x, x, x, x, x, x, x)
    print(x)
    x = x * 2
