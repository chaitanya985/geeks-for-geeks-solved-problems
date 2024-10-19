#User function Template for python3
from bisect import bisect_left

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, a):
        # code here
        
        List=[]
        
        for num in a:
            
            res=bisect_left(List, num)
            
            if res==len(List):
                
                List.append(num)
                
            else:
                
                List[res]=num
                
        return len(List)
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence(n, a))

# } Driver Code Ends