# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-3-worst-case-linear-time/

1) general sort
2) minHeap, maxHeap
3)Quick select and optimized quick select

# from heapq import *;
# def kthSmallest(arr, n, k): # max Heap
#     maxHeap = []
#     for i in range(k):
#         heappush(maxHeap, -arr[i])
#     for i in range(k, len(arr)):
#         if -arr[i] > maxHeap[0]:
#             heappop(maxHeap)
#             heappush(maxHeap, -arr[i])
#     print(-maxHeap[0])
#  O(K*logK+(N-K)*logK) = O(N∗logK), O(K)

# def kthLargest(arr, n, k):
#     arr.sort()
#     print(arr[n - k])

# def kthSmallest(arr, n, k):
#     arr.sort()
#     print(arr[k - 1])
# O(NlogN), O(N) timsort in python


arr = [12, 3, 5, 7, 19]
# [3, 5, 7, 12, 19]
n = len(arr)
k = 2
kthSmallest(arr, n, k)
#kthLargest(arr, n, k)