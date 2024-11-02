#User function Template for python3
from collections import defaultdict

class Solution:
    
    def diagonalSort(self, matrix, n, m):
        # code here 
        
        diagonals = defaultdict(list)
        
        for i in range (n):
        
            for j in range (m):
        
                diagonals[i-j].append(matrix[i][j])
                
        for key in diagonals:
        
            if key > 0:
        
                diagonals[key].sort()
        
            elif key < 0:
        
                diagonals[key].sort (reverse = True)
                
        for i in range (n):
        
            for j in range (m):
        
                matrix[i][j] = diagonals[i-j].pop(0)
                
        return matrix


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        inputLine = list(map(int, input().strip().split()))
        matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                matrix[i][j] = inputLine[i * m + j]
        ob=Solution()
        ob.diagonalSort(matrix,n,m)
        for i in range(n): 
            for j in range(m): 
                print(matrix[i][j], end =' ') 
            print() 
        tc-=1

        print("~")
# } Driver Code Ends