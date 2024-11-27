
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # code here
        
        seen=set()
        
        for num in arr:
            
            if num-x in seen or num+x in seen:
                
                return True
                
            seen.add(num)
            
        return False
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        x = int(input())

        obj = Solution()
        res = obj.findPair(arr, x)

        print("true" if res else "false")
        print("~")

# } Driver Code Ends