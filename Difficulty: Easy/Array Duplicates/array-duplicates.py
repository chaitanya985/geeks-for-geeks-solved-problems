
from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        duplicate=[]
        
        for i in range(n):
            
            if arr[abs(arr[i])] >= 0:
                
                arr[abs(arr[i])] -= arr[abs(arr[i])]
                
            else:
                duplicate.append(abs(arr[i]))
                
        if not duplicate:
            
            return [-1]
            
        return sorted(duplicate)
        



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

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends