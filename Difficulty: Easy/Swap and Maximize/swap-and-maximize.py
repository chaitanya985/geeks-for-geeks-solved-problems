#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        
        sum=0
        
        n=len(arr)
        
        arr.sort()
        
        for i in range(len(arr)//2):
            
            sum-=(2*arr[i])
            
            sum+=(2*arr[n-i-1])
            
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result


if __name__ == "__main__":
    main()

# } Driver Code Ends