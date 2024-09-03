#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos, neg=[], []
        
        for num in arr:
            
            (pos if num >= 0 else neg).append(num)
            
        arr[:]=[val for pair in zip(pos, neg) for val in pair] + pos[len(neg):] + neg[len(pos):]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    if tc == 1:
        print(-1)
    else:
        while tc > 0:
            arr = list(map(int, input().strip().split()))
            ob = Solution()
            ob.rearrange(arr)
            for x in arr:
                print(x, end=" ")
            print()
            tc -= 1

# } Driver Code Ends