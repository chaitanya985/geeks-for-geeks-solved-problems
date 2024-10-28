
from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        # code here
        
        dp = [[0] * (w + 1) for _ in range(n + 1)]
        
        for i in range(1, w + 1):
        
            dp[0][i] = float('inf')
        
        for i in range(1, n + 1):
        
            for j in range(1, w + 1):
        
                dp[i][j] = dp[i-1][j] if cost[i-1] == -1 or j < i else min(dp[i-1][j], cost[i-1] + dp[i][j-i])
        
        return -1 if dp[n][w] in (float('inf'), 0) else dp[n][w]
                    
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

        print("~")
# } Driver Code Ends