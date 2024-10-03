#User function Template for python3
class Solution:
    def valid(self, s): 
        #code here
        
        d={'(':')', '[':']', '{':'}'}
        
        stack=[]
        
        for i in s:
            
            if i in d:
                
                stack.append(i)
                
            else:
                
                if stack and d[stack[-1]] == i:
                    
                    stack.pop()
                    
                else:
                    
                    return 0
                    
        if len(stack)==0:
            
            return 1
            
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        if ob.valid(s):
            print(1)
        else:
            print(0)
# } Driver Code Ends