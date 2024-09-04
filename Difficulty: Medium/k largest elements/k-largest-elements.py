#User function Template for python3
import heapq

class Solution:

	def kLargest(self,arr, n, k):
		# code here
		
		res=[]
		
		for num in arr:
		    
		    if len(res) < k:
		        
		        heapq.heappush(res,num)
		        
		    elif res[0] < num:
		        
		        heapq.heappop(res)
		        
		        heapq.heappush(res, num)
		        
        return sorted(res, reverse=True)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends