print(69 // (10 if 4 > 0 else 6)) # 6
print(69 // (10 if 4 < 0 else 6)) # 11
print((69 if 4 > 0 else 7) // 5) # 13
print((69 if 4 < 0 else 7) // 5) # 1
print((69 if True else 7) // (69 if True else 7)) # 1
print((69 if True else 7) // (69 if False else 7)) # 9
print((69 if False else 7) // (69 if True else 7)) # 0
print((69 if False else 7) // (69 if False else 7)) # 1
