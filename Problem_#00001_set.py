arr = [10, 15, 3, 7]
k = 17
def loop():
    seen = set()
    for i in arr:
        if k - i in seen:
            return True
        seen.add(i)
    return False
print(loop())