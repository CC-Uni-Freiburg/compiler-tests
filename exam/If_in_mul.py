print(69 * (10 if 4 > 0 else 6)) # 690
print(69 * (10 if 4 < 0 else 6)) # 414
print((69 if 4 > 0 else 7) * 5) # 345
print((69 if 4 < 0 else 7) * 5) # 35
print((69 if True else 7) * (69 if True else 7)) # 4761
print((69 if True else 7) * (69 if False else 7)) # 483
print((69 if False else 7) * (69 if True else 7)) # 483
print((69 if False else 7) * (69 if False else 7)) # 49
