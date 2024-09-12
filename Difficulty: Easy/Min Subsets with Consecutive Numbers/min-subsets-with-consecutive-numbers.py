#User function Template for python3

class Solution:
    def numOfSubset(self, arr):
        # Your code goes here
        
        arr.sort()
        
        a=1
        
        for i in range(1, len(arr)):
            
            if arr[i]-arr[i-1] != 1:
                
                a+=1
                
        return a


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        ob = Solution()
        print(ob.numOfSubset(nums))


if __name__ == "__main__":
    main()

# } Driver Code Ends