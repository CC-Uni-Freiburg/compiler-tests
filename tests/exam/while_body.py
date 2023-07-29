# Author: Pascal Walter 4924063


def test() -> int:
    return 0


x = 0
while x < 42:
    a = -x - 1  # Will evaluate to -42
    b = True
    c = False if a < 0 else b
    d = a - a + 42  # Will evaluate to 42
    e = not a < 69
    if e or c:
        f = ([0, 1], [2, 3])
    else:
        f = ([4], [5])
    g = len(f)  # Will evaluate to 2
    h = len(f[0])  # Will evaluate to 2
    i = test()
    while i + test() < 2:
        i = i + 1  # i will evaluate to 1
    j = f[0][0]
    f[1][0] = 42
    k = input_int()  # in = 42
    x = x + 1

print(x)
print(a)
print(d)
print(g)
print(h)
print(i)
print(j)
print(f[1][0])
print(k)
