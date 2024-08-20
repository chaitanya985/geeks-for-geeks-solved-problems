#User function Template for python3

class Solution:
    
    def value(self, r):
        
        return {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}.get(r, -1)

    def romanToDecimal(self, S): 
        # code here
        res, i=0, 0
        
        while i < len(S):
            
            s1=self.value(S[i])
            
            s2=self.value(S[i+1]) if i+1 < len(S) else 0
            
            res+=s1 if s1 >= s2 else s2-s1
            
            i+= 1 if s1 >= s2 else 2
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends