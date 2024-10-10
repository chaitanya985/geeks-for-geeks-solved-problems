#User function Template for python3

class Solution:
    def isGoodorBad(self, S):
        # code here 
        
        v=0
        
        c=0
        
        for i in S:
            
            if i in 'aeiou':
                
                v+=1
                
                c=0
                
            elif i=='?':
                
                v+=1
                
                c+=1
                
            else:
                
                c+=1
                
                v=0
                
            if v > 5 or c > 3:
                
                return 0
                
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.isGoodorBad(S))
# } Driver Code Ends