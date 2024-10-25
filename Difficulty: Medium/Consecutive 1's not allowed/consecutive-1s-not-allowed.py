#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
    	
    	mod=10**9+7
    	
    	if n==1:
    	    
    	    return 2
    	    
    	if n==2:
    	    
    	    return 3
    	    
	    prev2=2
	    
	    prev1=3
	    
	    for i in range(3, n+1):
	        
	        curr=(prev1 + prev2) % mod
	        
	        prev2=prev1 % mod
	        
	        prev1=curr%mod
	        
        return prev1


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
        print("~")
# } Driver Code Ends