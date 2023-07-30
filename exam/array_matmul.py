# Author: Pascal Walter 4924063
a = [3, 7, 2, 2]
b = [7, 2, 3, 2]
c = [0, 0, 0, 0]

i = 0
while i < 2:
    j = 0
    while j < 2:
        k = 0
        while k < 2:
            c[2*i + j] = c[2*i + j] + (a[2*i + k] * b[2*k + j])
            k = k + 1
        j = j + 1
    i = i + 1
print(c[0])
