# Author: Pascal Walter 4924063
def func(x: list[list[int]]) -> int:
    x[0] = [42]
    return x[0][0]


def inc2DVec(vec: list[int]) -> list[int]:
    return [vec[0]+1, vec[1] + 1]


print(func([[0]]))
vec2d = [41, 41]
print(inc2DVec(vec2d)[0])
