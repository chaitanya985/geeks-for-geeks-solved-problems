#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def nextGreatest(self,arr):
		# code  here
		
		high=arr[-1]
		
		for i in range(len(arr)-2, -1, -1):
		    
		    temp=arr[i]
		    
		    arr[i]=high
		    
		    high=max(high, temp)
		    
	    arr[-1]=-1
	    
	    return arr

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.nextGreatest(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends