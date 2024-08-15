#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		max_prod = min_val = max_val = arr[0]
		
		for i in arr[1:]:
		    
		    if i < 0:
		        
		        max_val, min_val = min_val, max_val
		        
	        max_val = max(i, max_val * i)
	        
	        min_val = min(i, min_val * i)
	        
	        max_prod = max(max_prod, max_val)
		        
        return max_prod


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends