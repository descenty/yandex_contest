def func():
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n == 1:
        return 0
    counter = 0
    k = 0
    offset = 0
    while True:
        while arr[k] == arr[0]:
            k += 1
            if k == n:
                return counter
            if arr[k] < arr[k - 1]:
                return -1
        counter += arr[k] - arr[k - 1]
        for i in range(offset - 1, k):
            arr[i] = arr[k]
        offset = k - 1
        print(offset)


def func2():
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n == 1:
        return 0
    counter = 0
    offset = 0
    while len(arr) > 1:
        k = 0
        while arr[k] == arr[0]:
            k += 1
            if arr[k] < arr[k - 1]:
                return -1
        counter += arr[k] - arr[k - 1]
        print(arr)
        for i in range(k):
            del arr[i]
        print(arr)
    return counter

print(func2())