#User function Template for python3
class Solution:

	def findLargest(self,arr):
	    # code here
	    
	    num=[str(res) for res in arr]
	    
	    num.sort(key=lambda x:x*10, reverse=True)
	    
	    if num[0]=='0':
	        
	        return '0'
	        
	    ans=''.join(num)
	    
	    return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends