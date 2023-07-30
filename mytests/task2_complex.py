# in=1
# in=2
# in=3
# in=4
# in=5
# in=6
# in=-10
# golden=1 3
def func(x: int) -> int:
    while x != 0:
        if x < 0:
            print(1)
            return 20
        x = x - 1
    return x


i = 2
count = 0
while func(input_int()) < i:
    i = i + 1
    j = 0
    k = 1
    while (j if (i % 2) == 0 else k * k // k) == (len((1,)) - 1):
        j = k * 2
        count = count + 1

print(count)

while True:
    return 0
