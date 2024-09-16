#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        
        n=len(S)
        
        res=0
        
        l,r=0,0
        
        store=set()
        
        while r<n:
        
            while S[r] in store:
        
                store.remove(S[l])
        
                l+=1
        
            store.add(S[r])
        
            r+=1
        
            res=max(res,len(store))
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends