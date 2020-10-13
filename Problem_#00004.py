arr = [3, 4, -1, 1]

def missing_data():
    s = set(arr)
    i = 1
    while i in s:
        i+=1
    return i

print(missing_data())