# Author: Pascal Walter 4924063
def mod100(x: int) -> int:
    y = 7 % 8
    return x % 100


print(mod100(342 % 200) % 100)
