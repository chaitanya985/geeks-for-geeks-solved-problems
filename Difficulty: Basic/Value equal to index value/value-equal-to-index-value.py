#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        
        return [i+1 for i in range(len(arr)) if arr[i]==i+1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends