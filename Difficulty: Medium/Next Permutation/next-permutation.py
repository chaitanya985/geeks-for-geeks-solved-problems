#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        
        ind=0
        
        l=[]
        
        l+=arr
        
        for i in range(N-2, -1, -1):
            
            if l[i] < l[i+1]:
                
                ind=i
                
                break
            
        for i in range(N-1, ind, -1):
            
            if l[i] > l[ind]:
                
                l[i],l[ind]=l[ind],l[i]
                
                ind+=1
                
                break
            
        for i in range((N-ind)//2):
            
            l[i+ind], l[N-i-1] = l[N-i-1], l[i+ind]

        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends