#User function Template for python3

class Solution:
    def find_missing(self, arr):
        # code here
        
        n = len(arr) + 1
        
        exp = n * (arr[0] + arr[-1]) // 2
        
        val = exp - sum(arr)
        
        return val


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.find_missing(arr))


if __name__ == "__main__":
    main()

# } Driver Code Ends