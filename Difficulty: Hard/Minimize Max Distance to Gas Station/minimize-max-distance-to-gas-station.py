#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def Count(self, arr, K, mid):
        
        count = 0
        
        n = len(arr)
        
        for i in range(1, n):
        
            diff = arr[i] - arr[i - 1]
        
            if diff > mid:
        
                count += math.ceil(diff / mid) - 1
        
        return count <= K
        
    def findSmallestMaxDist(self, stations, K):
        
        n = len(stations)
        
        low = 0
        
        ans = 0
        
        high = stations[n - 1] - stations[0]
        
        while low <= high:
        
            mid = (low + high) / 2
        
            if self.Count(stations, K, mid):
        
                ans = mid
        
                high = mid - 0.000001
        
            else:
        
                low = mid + 0.000001
        
        return ans

#{ 
 # Driver Code Starts.
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
# } Driver Code Ends