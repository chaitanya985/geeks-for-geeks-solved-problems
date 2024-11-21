#User function Template for python3

class Solution:
    
    def largestNum(self,n,s):
        
        # code here
        if s < 0 or s > 9 * n:
            
            return "-1"
        
        result = []
        
        for i in range(n):
            
            digit = min(9, s)
            
            result.append(str(digit))
            
            s -= digit  
            
        return ''.join(result)

sol = Solution()
    
    


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
        print("~")
# } Driver Code Ends