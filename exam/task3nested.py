# Author: Alexander Pfefferle
# in=
# golden=1233
a = [([([[1, 2, 3]],)],)]
print(a[0][0][0][0][0][0])
print(a[0][0][0][0][0][1])


def modify_and_return(
    x: list[tuple[list[tuple[list[list[int]]]]]],
) -> list[tuple[list[tuple[list[list[int]]]]]]:
    x[0][0][0][0][0][0] = x[0][0][0][0][0][2]
    return x


b = modify_and_return(a)
# print(1 if a is b else 0)
# print(1 if (1,) is (2,) else 1) # support code doesn't support "is" for tuples
print([b][0][0][0][0][0][0][0])
print(len(a[0][0][0][0][0]))
