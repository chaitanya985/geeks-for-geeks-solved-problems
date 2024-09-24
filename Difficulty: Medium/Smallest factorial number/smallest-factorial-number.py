#User function Template for python3

class Solution:
    def findNum(self, n : int):
        # Complete this function
        
        def count(number):
            
            c=0
            
            while number>0:
                
                c+=number//5
                
                number//=5
                
            return c
            
        l, h=0, 5*n
        
        while l<h:
            
            mid=(l+h)//2
            
            if count(mid) >= n:
                
                h=mid
                
            else:
                l=mid+1
                
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends