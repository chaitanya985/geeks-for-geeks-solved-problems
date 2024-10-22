#User function Template for python3

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        
        dp=[[[0] * (n3+1) for _ in range(n2+1)] for _ in range(n1+1)]
        
        for i in range(1, n1+1):
            
            for j in range(1, n2+1):
                
                for k in range(1, n3+1):
                    
                    if A[i-1] == B[j-1] == C[k-1]:
                        
                        dp[i][j][k]=dp[i-1][j-1][k-1]+1
                        
                    else:
                        dp[i][j][k]=max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                        
        return dp[n1][n2][n3]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends