#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        # Complete the function
        arr.sort()
        
        return sum(arr[i] * i for i in range(len(arr))) % 1000000007
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends