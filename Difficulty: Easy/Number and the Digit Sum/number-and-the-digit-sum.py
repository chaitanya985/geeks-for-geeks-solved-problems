#User function Template for python3

class Solution:
    def numberCount(self,n,k):
    # code here
    
        def sum_of_digits(num):
            
            total=0
            
            while num > 0:
                
                total += num % 10
                
                num=num // 10
                
            return total
            
        l,r=1, n
        
        while l <= r:
            
            mid=(l+r)//2
            
            if (mid - sum_of_digits(mid) >= k):
                
                r=mid-1
                
            else:
                l=mid+1
                
        return n-l+1
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,k = ( int(x) for x in input().split() )
        ob = Solution()
        print(ob.numberCount(n,k))
# } Driver Code Ends