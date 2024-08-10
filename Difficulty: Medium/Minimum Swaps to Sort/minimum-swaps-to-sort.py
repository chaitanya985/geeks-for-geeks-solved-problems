

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		sorted_nums=sorted(enumerate(nums),key=lambda x:x[1])
		
		swaps=0
		
		visited=[False]*len(nums)
		
    	for i in range(len(nums)):
    		
	        if visited[i] or sorted_nums[i][0]==i:
		
		        continue
	
		    cycle_size=0
    		
		    j=i
    		
    		while not visited[j]:
    		    
    		    visited[j]=True
    		    
    		    j=sorted_nums[j][0]
    		    
    		    cycle_size+=1
    		    
    	    swaps+=cycle_size-1
    
        return swaps
		
		
		


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends