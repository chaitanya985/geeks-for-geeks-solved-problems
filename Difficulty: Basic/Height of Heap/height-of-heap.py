# User function Template for Python3

class Solution:
    def heapHeight(self, N, arr):
        # code here
        
        if N==1:
            
            return 1
            
        N-=1
        
        count=0
        
        while N > 0:
            
            count+=1
            
            N=(N-1)//2
            
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.heapHeight(N, arr))

# } Driver Code Ends