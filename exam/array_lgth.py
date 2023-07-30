# Author: Pascal Walter 4924063
def get_len(arr: list[int]) -> int:
    return len(arr)


print(len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
           22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]))

x = [1, 2]
print(len(x) + 40)

print(get_len(x) + 40)

if len([[123], [4, 5, 6]][1]) > 2:
    y = (len(x) + 1) * 2 * 7 * 2 // 2 % 100
else:
    y = (0 if len(x) > 0 else 420)

print(y)
