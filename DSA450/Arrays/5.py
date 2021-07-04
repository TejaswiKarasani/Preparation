# 1. using quick sort
# 2. using two pointer TODO

def rearrange(arr, n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            swap(arr, i, j)
            j += 1
    print(arr)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
# O(N), O(1)
            


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)