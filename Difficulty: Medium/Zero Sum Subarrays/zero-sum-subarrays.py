#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        c, sum1, hashMap = 0, 0, {}
        
        for i in range(n):
        
            sum1 += arr[i]
        
            if sum1 == 0: c += 1
        
            if sum1 in hashMap: c += len(hashMap[sum1])
        
            hashMap[sum1] = hashMap.get(sum1, []) + [i]
        
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends