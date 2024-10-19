#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        
        n1 = len(s1)
        
        n2 = len(s2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        ans = 0
        
        for i in range(1, n1 + 1):
        
            for j in range(1, n2 + 1):
        
                if s1[i - 1] == s2[j - 1]:
        
                    dp[i][j] = 1 + dp[i - 1][j - 1]
        
                    ans = max(ans, dp[i][j])
        
                else:
        
                    dp[i][j] = 0
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends