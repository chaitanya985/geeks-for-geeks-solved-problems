#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        
        if n < 3:
            
            return -1
            
        arr.sort()
        
        ans=max(arr[0]*arr[1]*arr[n-1], arr[n-1]*arr[n-2]*arr[n-3])
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletProduct(arr, n)
    print(res)
    print("~")
# } Driver Code Ends