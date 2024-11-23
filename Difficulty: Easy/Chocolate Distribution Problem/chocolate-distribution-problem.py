#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        arr.sort()
        
        mindiff=100000
        
        l, r=0, M-1
        
        while r < len(arr):
            
            diff=arr[r] - arr[l]
            
            mindiff=min(diff,mindiff)
            
            l+=1
            
            r+=1
            
        return mindiff
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        A = [int(x) for x in input().split()]
        M = int(input())

        solObj = Solution()

        print(solObj.findMinDiff(A, M))
        print("~")

# } Driver Code Ends