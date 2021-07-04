# read the time complexities in detail
def maxMin(arr):
    n = len(arr)
    if n % 2 == 0:
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i = 2
    else:
        mx, mn = arr[0], arr[0]
        i = 1
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
        i += 2
    print([mx, mn])


# def maxMin(arr):
#         result = getMaxMin(arr, 0, len(arr) - 1)
#         print(result)

# def getMaxMin(arr, low, high):
#     arr_max, arr_min = arr[low], arr[low]
#     if low == high:
#         arr_max, arr_min = arr[low], arr[low]
#         return [arr_max, arr_min]
#     elif high == low + 1:
#         if arr[low] > arr[high]:
#             arr_max, arr_min = arr[low], arr[high]
#         else:
#             arr_max, arr_min = arr[high], arr[low]
#         return [arr_max, arr_min]
#     else:
#         mid = (low + high)//2
#         arr_max1, arr_min1 = getMaxMin(arr, low, mid)
#         arr_max2, arr_min2 = getMaxMin(arr, mid + 1, high)
#     return [max(arr_max1, arr_max2), min(arr_min1, arr_min2)]


# def maxMin(n):
#     minEle = float("inf")
#     maxEle = float("-inf")
#     for ele in n:
#         if ele < minEle:
#             minEle = ele
#         if ele > maxEle:
#             maxEle = ele
#     print([minEle, maxEle])
# TC, SC: O(N), O(1)
maxMin([1, 2, 3, -1, 4, 10])