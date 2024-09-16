#User function Template for python3
class Solution:
    def metaStrings(self, S1, S2):
        # code here
        
        if len(S1) != len(S2) or set(S1) != set(S2):
            
            return 0
            
        count=sum(same1 != same2 for same1, same2 in zip(S1, S2))
        
        if count==2:
            
            return 1
            
        else:
            
            return 0
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        obj = Solution()
        if obj.metaStrings(S1, S2):
            print(1)
        else:
            print(0)
# } Driver Code Ends