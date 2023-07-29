# Author: Pascal Walter 4924063
bin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x = input_int()
i = 0
while x > 1:
    y = x % 2
    x = x // 2
    bin[i] = y
    i = i + 1
if x == 1:
    bin[i] = 1

i = len(bin) - 1
while i >= 0:
    print(bin[i])
    i = i - 1
