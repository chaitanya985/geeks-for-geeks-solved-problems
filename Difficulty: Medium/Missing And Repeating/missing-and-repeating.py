#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        seen = set()
        
        repeat = 0
        
        total_sum = n * (n + 1) // 2
        
        array_sum = sum(arr)
        
        for num in arr:
        
            if num in seen:
        
                repeat = num
        
            seen.add(num)
        
        missing = total_sum - (array_sum - repeat)
        
        return [repeat, missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends