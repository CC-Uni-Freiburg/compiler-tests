a = 3776030
b = -3776030
c = 87905
d = -87905
e = 0
print(a % a) # 0
print(a % b) # 0 
print(a % c) # 84020
print(a % d) # 84020
print(b % a) # 0
print(b % b) # 0
print(b % c) # -84020
print(b % d) # -84020
print(c % a) # 87905
print(c % b) # 87905
print(c % c) # 0
print(c % d) # 0
print(d % a) # -87905
print(d % b) # -87905
print(d % c) # 0
print(d % d) # 0
print(e % a) # 0
print(e % b) # 0
print(e % c) # 0
print(e % d) # 0
# Jetzt nochmal alles für die größten Zahlen.
a = 9223372036854775807
b = -9223372036854775807
print(a % a) # 0
print(a % b) # 0
print(b % a) # 0
print(b % b) # 0
print(e % a) # 0
print(e % b) # 0
