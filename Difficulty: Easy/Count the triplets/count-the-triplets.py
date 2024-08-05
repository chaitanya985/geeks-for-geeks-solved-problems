# User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
		# code here
		arr.sort()
        count = 0
        for i in range(n - 1, 1, -1):
            j = 0
            k = i - 1
            while j < k:
                if arr[j] + arr[k] == arr[i]:
                    count += 1
                    j += 1
                    k -= 1
                elif arr[j] + arr[k] < arr[i]:
                    j += 1
                else:
                    k -= 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends