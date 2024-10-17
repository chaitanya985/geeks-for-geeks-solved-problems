
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        
        curr=1
        
        prev=1
        
        for i in range(n-2):
            
            curr, prev=(curr+prev)%1000000007, curr
            
        return curr
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends