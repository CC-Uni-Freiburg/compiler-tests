#in=
#golden=42
def ret_42() -> int:
    x = 0
    while True:
        if x == 42:
            return 42
        else:
            x = x + 1
    return 42


print(ret_42())
