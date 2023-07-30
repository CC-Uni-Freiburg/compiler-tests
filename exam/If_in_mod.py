print(69 % (10 if 4 > 0 else 6))  # 9
print(69 % (10 if 4 < 0 else 6))  # 3
print((69 if 4 > 0 else 7) % 5)  # 4
print((69 if 4 < 0 else 7) % 5)  # 2
print((69 if True else 7) % (69 if True else 7))  # 0
print((69 if True else 7) % (69 if False else 7))  # 6
print((69 if False else 7) % (69 if True else 7))  # 7
print((69 if False else 7) % (69 if False else 7))  # 0
