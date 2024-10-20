#User function Template for python3

class Solution:
    def LCIS(self, arr1, arr2):
        # code here
        
        n=len(arr1)
        
        m=len(arr2)
        
        dp=[0]*m
        
        res=0
        
        for i in range(n):
            
            max_len=0
            
            for j in range(m):
                
                if arr1[i]==arr2[j]:
                    
                    dp[j]=max(dp[j], max_len+1)
                    
                elif arr1[i] > arr2[j]:
                    
                    max_len=max(max_len, dp[j])
                    
            res=max(res, max(dp))
            
        return res


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.LCIS(arr1, arr2))

# } Driver Code Ends