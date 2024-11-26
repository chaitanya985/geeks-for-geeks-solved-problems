#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        
        n=len(grid)
        
        m=len(grid[0])
        
        def dfs(x, y):
            
            if x < 0 or y < 0 or x >= n or y >= m or grid[x][y]==0:
                
                return
            
            grid[x][y]=0
            
            direction=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for my, mx in direction:
                
                dfs(x+mx, y+my)
                
        island=0
        
        for i in range(n):
            
            for j in range(m):
                
                if grid[i][j]==1:
                    
                    island+=1
                    
                    dfs(i, j)
                    
        return island


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends