# solve using Dutch Flag Algorithms 3 pointers approach also!
class Solution:
    def sort012(self,arr,n):
        # code here
        count = [0, 0, 0]
        for ele in arr:
            if ele == 0:
                count[ele] += 1
            elif ele == 1:
                count[ele] += 1
            elif ele == 2:
                count[ele] += 1
        for i in range(len(arr)):
            if i < count[0]:
                arr[i] = 0
            elif i < count[0] + count[1] and i >= count[0]:
                arr[i] = 1
            else:
                arr[i] = 2