#User function Template for python3
class Solution:
	def isRepeat(self, s):
		# code here
		
		double_str=(s+s)[1:-1]
		
		if s in double_str:
		    
		    return 1
		    
	    else:
	        
	        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isRepeat(s)
		
		print(answer)


# } Driver Code Ends