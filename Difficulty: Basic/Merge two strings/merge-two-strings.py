#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        # code here
        
        alt=""
        
        for i in range(max(len(S1), len(S2))):
            
            if i < len(S1):
                
                alt+=S1[i]
                
            if i < len(S2):
                
                alt+=S2[i]
                
        return alt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
# } Driver Code Ends