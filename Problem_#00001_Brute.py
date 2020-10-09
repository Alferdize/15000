#  Brute Force 
arr = [10, 15, 3, 7]
k = 17

def loop():
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == k:
                return True
    return False

print(loop())