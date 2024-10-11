#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        # code here
        
        arr.sort(key=lambda item: item.value / item.weight, reverse=True)
        
        weight_remain = w
        
        value_sum = 0
        
        for i in range(n):
        
            if weight_remain >= arr[i].weight:
        
                weight_remain -= arr[i].weight
        
                value_sum += arr[i].value
        
            else:
        
                value_sum += weight_remain * arr[i].value / arr[i].weight
        
                return value_sum
        
        return value_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


class Item:

    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, w = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(w, arr, n))

# } Driver Code Ends