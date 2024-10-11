#User function Template for python3

class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        
        # code here
        
        if (s==0 and n==1):
            
            return '0'
            
        if (s>9*n):
            
            return '-1'
            
        password=[]
        
        for i in range(n):
            
            if s>9:
                
                password.append('9')
                
                s-=9
                
            else:
                
                password.append(str(s))
                
                s=0
                
        return ''.join(password)
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends