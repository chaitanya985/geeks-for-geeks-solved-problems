#User function Template for python3

class Solution:
        #code here
    def pr(self, string, n, x):
        
        result = 0
        
        stack = []
        
        for i in range(n):
        
            if string[i] == 'r' and len(stack) != 0 and stack[-1] == 'p':
        
                    stack.pop(-1)
        
                    result += x
        
            else:
        
                stack.append(string[i])
        
        return result, "".join(stack)
    
    def rp(self, string, n, y):
        
        result = 0
        
        stack = []
        for i in range(n):
        
            if string[i] == 'p' and len(stack) != 0 and stack[-1] == 'r':
        
                    stack.pop(-1)
        
                    result += y
        
            else:
        
                stack.append(string[i])
        
        return result, "".join(stack) 
            
        
    def solve (self, X, Y, S):
        #code here
        if X > Y:
        
            result, remainingString = self.pr(S, len(S), X)
        
            result += self.rp(remainingString, len(remainingString), Y)[0]
        
        else:
        
            result, remainingString = self.rp(S, len(S), Y)
        
            result += self.pr(remainingString, len(remainingString), X)[0]
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()
        

        ob = Solution()
        print(ob.solve(X,Y,S))
# } Driver Code Ends