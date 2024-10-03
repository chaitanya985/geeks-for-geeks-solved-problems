#User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        # code here
        
        stack=[]
        
        for i in S:
            
            while stack and int(stack[-1]) > int(i) and K>0:
                
                stack.pop()
                
                K-=1
                
            stack.append(i)
            
        while K>0:
            
            stack.pop()
            
            K-=1
            
        ans=''.join(stack).lstrip('0')
        
        if ans:
            
            return ans
            
        else:
            return '0'
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends