#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        
        arr.sort()
        
        n=len(arr)
        
        maxa=arr[n-1]
        
        mina=arr[0]
        
        ans=maxa-mina
        
        for i in range(len(arr)):
            
            maxa=max(arr[i-1]+k, arr[n-1]-k)
            
            mina=min(arr[0]+k, arr[i]-k)
            
            ans=min(maxa-mina, ans)
            
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)

# } Driver Code Ends