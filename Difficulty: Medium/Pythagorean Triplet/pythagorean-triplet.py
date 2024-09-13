#User function Template for python3
class Solution:

	def checkTriplet(self,arr, n):
    	# code here
    	
    	triplet={i*i: i for i in arr}
    	
    	for a in triplet:
    	    
    	    for b in triplet:
    	        
    	        if (a+b) in triplet:
    	            
    	            return True
    	            
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends