#User function Template for python3

class Solution:
    def sortIt(self, arr):
        #code here.
        
        arr.sort()
        
        odd=[i for i in arr if i % 2 == 1]
        
        even=[i for i in arr if i % 2 == 0]
        
        odd.reverse()
        
        final=odd+even
        
        arr[:]=final[:]
    



#{ 
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(arr)
        print(*arr)
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends