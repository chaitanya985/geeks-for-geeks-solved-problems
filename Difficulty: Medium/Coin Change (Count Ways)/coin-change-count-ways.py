#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        # code here 
        
        table = [[0] * N for _ in range(sum + 1)]
        
        for i in range(N):
        
            table[0][i] = 1
        
        for i in range(1, sum + 1):
        
            for j in range(N):
        
                x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0
        
                y = table[i][j - 1] if j >= 1 else 0
        
                table[i][j] = x + y
        
        return table[sum][N - 1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends