#User function Template for python3
import heapq

class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr):
    
       heapq.heapify(arr)
       
       ans=0
       
       while len(arr)>=2:
       
           s1=heapq.heappop(arr)
       
           s2=heapq.heappop(arr)
       
           ans=ans+s1+s2
       
           heapq.heappush(arr,s1+s2)
       
       return ans
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends