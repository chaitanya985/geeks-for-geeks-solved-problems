#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        arr.sort()
        
        n, result = len(arr), []
        
        for i in range(n - 3):
        
            if i > 0 and arr[i] == arr[i - 1]: continue
        
            for j in range(i + 1, n - 2):
        
                if j > i + 1 and arr[j] == arr[j - 1]: continue
        
                left, right = j + 1, n - 1
        
                while left < right:
        
                    total = arr[i] + arr[j] + arr[left] + arr[right]
        
                    if total == k:
        
                        result.append([arr[i], arr[j], arr[left], arr[right]])
        
                        while left < right and arr[left] == arr[left + 1]: left += 1
        
                        while left < right and arr[right] == arr[right - 1]: right -= 1
        
                        left += 1; right -= 1
        
                    elif total < k: left += 1
        
                    else: right -= 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.fourSum(A, D)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print()
        if (len(ans) == 0):
            print(-1)
        # print()

# } Driver Code Ends