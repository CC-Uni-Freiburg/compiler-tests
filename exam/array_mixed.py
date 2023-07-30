# Author: Pascal Walter 4924063
def ret_42(m: int) -> int:
    return ((42 * m) // m)


def test_everything(n: int) -> int:
    y = ([(1,)], ([2, 3], [41, n]))
    while y[1][1][0] != 42:
        y[1][1][0] = ret_42(len(y))
    return y[1][1][0]


x = 7
print(test_everything(x))
