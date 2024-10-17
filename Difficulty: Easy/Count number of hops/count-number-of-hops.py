#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        # code here
        
        mod=1000000007
        
        if n==1:
            
            return 1
            
        if n==2:
            
            return 2
            
        if n==3:
            
            return 4
            
        a=1
        
        b=2
        
        c=4
        
        for i in range(4, n+1):
            
            temp=(a+b+c)%mod
            
            a=b
            
            b=c
            
            c=temp
            
        return temp
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends