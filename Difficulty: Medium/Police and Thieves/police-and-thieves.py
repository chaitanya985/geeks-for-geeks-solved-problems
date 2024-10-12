#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import deque

class Solution:
    def catchThieves(self, arr, n, k): 
        # code here 
        
        police = deque()
        
        thieves = deque()
        
        for i in range(n):
        
            if arr[i] == 'P':
        
                police.append(i)
        
            else:
        
                thieves.append(i)
        
        count = 0
        
        while len(police) and len(thieves):
            
            if abs(police[0] - thieves[0]) <= k:
        
                police.popleft()
        
                thieves.popleft()
        
                count += 1
        
            else:
        
                if police[0] < thieves[0]:
        
                    police.popleft()
        
                else:
        
                    thieves.popleft()
                
        return count

#{ 
 # Driver Code Starts.

if __name__=='__main__': 
	t = int(input())
	for _ in range(t):
		line1 = list(map(int, input().strip().split()))
		n = line1[0]
		k = line1[1]
		arr = list(input().strip().split())
		obj = Solution()
		print(obj.catchThieves(arr, n, k))


# } Driver Code Ends