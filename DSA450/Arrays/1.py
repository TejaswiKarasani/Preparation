def reverseArray(n):
    result = reverseArrayHelper(n, 0, len(n) - 1)
    print(result)

def reverseArrayHelper(A, start, end):
    if start >= end:
        return n
    A[start], A[end] = A[end], A[start]
    #print(A)
    reverseArrayHelper(A, start+1, end-1)
# Not working, complexity not sure; O(N), O(N) - 



# def reverseArray(n):
#     first, last = 0, len(n) - 1
#     while first < last:
#         swap(first, last, n)
#         first += 1
#         last -= 1
#     print(n)

# def swap(a, b, arr):
#     arr[a], arr[b] = arr[b], arr[a]
# O(N/2) ~ O(N), O(1)

# def reverseArray(n):
#     n1 = []
#     for i in reversed(range(len(n))):
#         n1.append(n[i])
#     print(n1)
# O(N), O(N)

n = [1, 2, 3, 4, 5]
reverseArray(n)