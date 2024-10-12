#User function Template for python3
import bisect

class Solution:
    def minSteps(self, arr, n, k):
        # code here 
        
        ret=float('inf')
        
        arr.sort()
        
        pref_sum=[0]
        
        for a in arr:
        
            pref_sum.append(pref_sum[-1]+a)
        
        l_bond=0
        
        prev=-1
        
        for a in range(n):
            
            if prev==arr[a]:
        
                continue
            
            target=arr[a]+k
            
            pos=bisect.bisect_right(arr[l_bond:],target)+l_bond
            
            l_bond=pos
            
            right_coins=(pref_sum[-1]-pref_sum[pos])-(arr[a]+k)*(n-pos)
            
            left_coins=pref_sum[a]
            
            ret=min(left_coins+right_coins,ret)
            
            prev=arr[a]
    
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for _ in range (t):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    
    ob = Solution()
    print(ob.minSteps(A,N,K))
# } Driver Code Ends