#User function Template for python3

class Solution:
    def Maximum_Sum(self, mat, N, K):
        # Your code goes here
        a = [[0] * (N + 1) for _ in range(N + 1)]
        
        max1=float('-inf')
        
        for i in range(1,N+1):
        
            for j in range(1,N+1):
        
                a[i][j] =(mat[i-1][j-1] +a[i-1][j]+a[i][j-1]-a[i-1][j-1])
        
                if (i>=k and j>=k):
        
                    max1=max((a[i][j]-(a[i-k][j]+a[i][j-k] - a[i-k][j-k])),max1)
        
        return max1


#{ 
 # Driver Code Starts


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        matrix=[]
        for _ in range(n):
            matrix.append( [ int(x) for x in input().strip().split() ] )
        k=int(input())
        obj = Solution()
        print(obj.Maximum_Sum(matrix,n,k))
# } Driver Code Ends