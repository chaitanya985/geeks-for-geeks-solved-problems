#User function Template for python3

class Solution:
    
    def checkCompressed(self, S, T):
        # code here 
        
        i, j = 0, 0
        
        while i < len(S) and j < len(T):
        
            if T[j].isdigit():
        
                num = 0
        
                while j < len(T) and T[j].isdigit():
        
                    num = num * 10 + int(T[j])
        
                    j += 1
        
                i += num
        
            else:
        
                if i >= len(S) or S[i] != T[j]:
        
                    return 0
        
                i += 1
        
                j += 1
        
        return 1 if i == len(S) and j == len(T) else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        T = input()
        
        ob = Solution()
        print(ob.checkCompressed(S,T))
# } Driver Code Ends