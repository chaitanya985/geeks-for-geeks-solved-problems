#User function Template for python3
class Solution:
     
    # Should return true if there exists a triplet in the
    # array arr[] which sums to x. Otherwise false
    def find3Numbers(self, arr, n, x):
        # Your Code Here
        
        arr.sort()
        
        for i in range(n-2):
            
            l, r=i+1, n-1
            
            while l < r:
                
                curr_sum=arr[i]+arr[l]+arr[r]
                
                if curr_sum==x:
                    
                    return True
                    
                l+=(curr_sum < x)
                
                r-=(curr_sum > x)
                
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, X = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        if (ob.find3Numbers(A, n, X)):
            print(1)
        else:
            print(0)

# } Driver Code Ends