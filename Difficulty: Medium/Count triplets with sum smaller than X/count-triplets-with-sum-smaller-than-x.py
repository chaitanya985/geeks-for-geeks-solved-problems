class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        
        count=0
        
        arr.sort()
        
        for i in range(0,n-2):
            
            right = i+1
            
            left = n-1
            
            while right<left:
            
                temp = arr[i]+arr[left]+arr[right]
            
                if temp >= sum:
            
                    left -= 1
            
                else:
            
                    count += left-right
            
                    right += 1
        
        return count
            
            

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(0, t):
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    a = list(map(int, input().split()))
    ob = Solution()
    ans = ob.countTriplets(n, k, a)
    print(ans)

# } Driver Code Ends