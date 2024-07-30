#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix): 
        # code here 
        
        result=[]
        
        while matrix:
            
            result += matrix.pop(0)
            
            if matrix and matrix[0]:
                
                for row in matrix:
                    
                    result.append(row.pop())
                    
            if matrix:
                
                result += matrix.pop()[::-1]
                
            if matrix and matrix[0]:
                
                for row in matrix[::-1]:
                    
                    result.append(row.pop(0))
                    
        return result
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends