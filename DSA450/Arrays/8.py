class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        maxHere, maxSoFar = a[0], a[0]
        for i in range(1, size):
            maxHere = max(a[i], maxHere + a[i])
            maxSoFar = max(maxHere, maxSoFar)
        return maxSoFar
