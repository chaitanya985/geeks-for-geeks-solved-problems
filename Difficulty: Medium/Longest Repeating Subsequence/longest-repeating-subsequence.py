#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code here
		
		n=len(str)
		
		dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
		
		for i in range(1, n+1):
		    
		    for j in range(1, n+1):
		        
		        if str[i-1]==str[j-1] and i!=j:
		            
		            dp[i][j]=dp[i-1][j-1]+1
		            
	            else:
	                
	                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
	                
        return dp[n][n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends