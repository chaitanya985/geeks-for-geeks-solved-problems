#User function Template for python3

class Solution:
    def lengthOfLongestAP(self,arr):
        # code here

        n = len(arr)

        if n <= 2:

            return n

        dp = [[2 for _ in range(n)] for _ in range(n)]

        max_len = 2  

        for j in range(n-2, -1, -1):

            i = j - 1

            k = j + 1

            while i >= 0 and k < n:

                if arr[i] + arr[k] < 2 * arr[j]:

                    k += 1

                elif arr[i] + arr[k] > 2 * arr[j]:

                    dp[i][j] = 2

                    i -= 1

                else:

                    dp[i][j] = dp[j][k] + 1

                    max_len = max(max_len, dp[i][j])

                    i -= 1

                    k += 1

        return max_len


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.lengthOfLongestAP(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends