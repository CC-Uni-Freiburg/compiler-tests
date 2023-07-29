#in=
#golden=42 42 1 -1 3 3 1
def func1(a: list[list[list[int]]]) -> list[list[int]]:
    return a[0]

def func2(a: list[list[int]]) -> list[int]:
    return a[0]

def func3(a: list[int]) -> int:
    return a[0]

def gunc(a: tuple[int, int]) -> int:
    return a[0]

a = [[[42,3],[2]],[[4,4,5]],[[43]]]
print(a[0][0][0])
print(func3(func2(func1(a))))
[[[a]]][0][0][0][0][0] = [1,2]
print(func2(a[0])[0])
[[[[0]]], [a[0]]][1][0][0][0] = -1
print(a[0][0][0])
b = [([(3,2),(1,3)],4)]
print(b[0][0][0][0])
print(gunc(b[0][0][0]))
print(len([len([len([len(a), len(b)])])]))
