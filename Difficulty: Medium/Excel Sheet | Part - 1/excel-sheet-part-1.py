#User function Template for python3

class Solution:
    def ExcelColumn(self, N):
        #return required string
        #code here
        check="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        check=list(check)
        
        strs=""
        
        while N>>0:
        
            N-=1
        
            rem=N%26
        
            strs = check[rem] + strs
            
            N=N//26
            
        return strs


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

        print("~")
# } Driver Code Ends