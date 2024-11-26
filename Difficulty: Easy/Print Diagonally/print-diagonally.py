#User function Template for python3

def downwardDiagonal(N, A): 
    # code here 
    
    res=[]
    
    for i in range(2*N-1):
        
        if i < N:
            
            col=i
            
            row=0
            
        else:
            col=n-1
            
            row=i-N+1
            
        while(row < n and col >= 0):
            
            res.append(A[row][col])
            
            row+=1
            
            col-=1
            
    return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDiagonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

        print("~")
# } Driver Code Ends