#User function Template for python3

class Solution:
    def longestPalin(self, S):
        # code here
        
        l=""
        
        if S==S[::-1]:
            
            return S
            
        for i in range(0, len(S)):
            
            for j in range(i+1, len(S)+1):
                
                a=S[i:j]
                
                if a==a[::-1]:
                    
                    if len(l) < len(a):
                    
                        l=a
                        
        if len(l)==1:
            
            return S[0]
            
        return l
                    
                
                    
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends