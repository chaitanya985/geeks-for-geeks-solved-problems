#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        arr=list(set(arr))
        
        arr.sort()
        
        if len(arr) < 2:
            
            return -1
            
        else:
            return arr[-2]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends