#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        
        mid=(sizeOfStack) // 2
        
        if (sizeOfStack % 2 == 0):
            
            del s[mid-1]
            
        else:
            
            del s[mid]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys

sys.setrecursionlimit(10**8)


def main():
    t = int(input())
    while (t > 0):
        sizeOfStack = int(input())
        myStack = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack, sizeOfStack)
        while (len(myStack) > 0):
            print(myStack[-1], end=" ")
            myStack.pop()
        print()
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends