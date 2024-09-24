#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        
        pos = []
        
        for i in arr:
       
            if i > 0:
       
                pos.append(i)
       
        f = len(pos) + 1
       
        return ((f * (f + 1)) // 2) - sum(pos)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    if (T == 2):
        print(-1)
    else:
        while (T > 0):
            arr = [int(x) for x in input().strip().split()]
            ob = Solution()
            print(ob.missingNumber(arr))
            T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends