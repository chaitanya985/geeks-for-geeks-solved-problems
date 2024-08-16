class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        
        a, b=0, n-1
        
        while a < b:
            
            a+=(mat[a][b]==1)
            
            b-=(mat[a][b]==0)
            
        return a if all(mat[a][i]==0 and mat[i][a]==1 for i in range(n) if i != a) else -1


#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends