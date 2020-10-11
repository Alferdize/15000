import math

EPS = 1e-9

arr = [1, 2, 3, 4, 5]



def productPuzzle():
    sum = 0
    for i in range(len(arr)):
        sum += math.log10(arr[i])

    data = []
    for i in range(len(arr)):
        data.append(int((EPS + pow(10.00, sum - math.log10(arr[i])))))

    return data


print(productPuzzle())