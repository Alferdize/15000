from bisect import bisect_left
arr = [10, 15, 3, 7]
k = 17

def two_sum():
    arr.sort()

    for i in range(len(arr)):
        target = k - arr[i]
        j = binary_search(arr, target)

        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(arr) and arr[j + 1] == target:
            return True
        elif j - 1 >= 0 and arr[j - 1] == target:
            return True
    return False



def binary_search(arr, target):
    lo = 0
    hi = len(arr)
    ind = bisect_left(arr, target, lo, hi)

    if 0 <= ind < hi and arr[ind] == target:
        return ind
    return -1

print(two_sum())