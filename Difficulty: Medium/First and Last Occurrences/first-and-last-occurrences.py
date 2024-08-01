#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        first=-1
        
        last=-1
        
        for i in range(n):
            
            if arr[i]==x:
                
                if first==-1:
                    
                    first=i
                    
                last=i
                
        return first, last


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends