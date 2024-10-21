class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,string):
        # Code here
        
        mod=10**9+7
        
        dp=[1]*len(string)
        
        for i in range(1, len(string)):
            
            c=1
            
            for j in range(i-1, -1, -1):
                
                t=dp[j]
                
                if string[i]==string[j]:
                    
                    dp[j]+=c
                    
                c+=(t%mod)
                
        return (sum(dp) % mod)



#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends