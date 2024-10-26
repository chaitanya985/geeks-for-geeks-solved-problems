#User function Template for python3

class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,N):
        # code here
        
        mod=10**9+7
        
        dp=[0]*(n+1)
        
        dp[0]=dp[1]=1
        
        for i in range(2, n+1):
            
            for j in range(1, i+1):
            
                dp[i]=dp[i]+(dp[i-j] * dp[j-1])
            
        return dp[n] % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n = int(input());
        ob=Solution()
        print(ob.numTrees(n))
        print("~")
# } Driver Code Ends