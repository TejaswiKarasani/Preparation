# 1. use set
# 2. use visited array by initializing max
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        #code here
        s = set()
        for ele1 in a:
            s.add(ele1)
        for ele2 in b:
            s.add(ele2)
        return len(s)
        