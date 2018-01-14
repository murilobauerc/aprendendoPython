
def fat(n):
    i = 1
    while i < n:
        fat = fat * i
        i += 1
    return fat
