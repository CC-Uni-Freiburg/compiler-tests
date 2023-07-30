# Author: Alexander Pfefferle
# in=
# golden=011706912
print(len([]))
print(len([1]))
a = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
print(len([a]))
print(len(a if len(a) - 5 == 65 else [1]))
if len(a) == 70:
    i = len(a) - 2 * (len(a) // 2)
    while i < len(a):
        a[i] = i
        i = i + 1
print(a[len(a) - 1])


def lentest(a: tuple[int, bool, list[int]], b: list[int]) -> int:
    if len(a) == len(b):
        return 1
    else:
        return 0


print(lentest((1, True, [3]), [1, 2, 3]))
print(len((1, 2)))
