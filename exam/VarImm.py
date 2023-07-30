a = 96
b = -96
c = 19
d = -19
e = 0
print(a % 19) # 1
print(96 % c) # 1
print(0 % c) # 0
print(e % 19) # 0
print(b % 19) # -1
print(-96 % c) # -1
print(a % -19) # 1
print(96 % d) # 1
print(b % -19) # -1
print(-96 % d) # -1
print(0 % d) # 0
print(e % -19) # 0
# Jetz nochmal alles für maximal große Werte.
a = 9223372036854775807
b = -9223372036854775807
print(a % -9223372036854775807) # 0
print(9223372036854775807 % b) # 0
print(b % 9223372036854775807) # 0
print(-9223372036854775807 % a) # 0
print(0 % b) # 0
print(0 % a) # 0
