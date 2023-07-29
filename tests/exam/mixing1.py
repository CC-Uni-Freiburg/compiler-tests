# Author: Pascal Walter 4924063
def test_operations(a: int, b: int, c: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a * b // 2 % 100, a // b * 10, a % b % 100)


def double(x: int) -> int:
    return x * 2


def half(x: int) -> int:
    return x // 2


x = 6
y = 7
z = (2 * 3, 19 // 2, 10 % 4)
z = test_operations(x, y, z)
print(-(double(z[0]) * half(z[1]) % z[2] + 10) * 4 // 2)
