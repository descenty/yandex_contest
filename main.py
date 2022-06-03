def func():
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n == 1:
        return 0
    counter = 0
    while len(arr) > 1:
        k = 0
        while k != len(arr) - 1 and arr[k] == arr[0]:
            k += 1
            if arr[k] < arr[k - 1]:
                return -1
        counter += arr[k] - arr[k - 1]
        for i in range(k):
            del arr[0]
    return counter

print(func())