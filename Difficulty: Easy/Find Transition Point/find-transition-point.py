class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        
        arr=[str(i) for i in arr]
        
        arr=''.join(arr)
        
        return arr.find('1')


#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends