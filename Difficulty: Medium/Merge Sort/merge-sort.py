#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        temp = []
        
        left = l
        
        right = m + 1 
        
        while left <= m and right <= r:
            
            if arr[left] <= arr[right]:
            
                temp.append(arr[left])
            
                left += 1
            
            else:
            
                temp.append(arr[right])
            
                right += 1
        
        while left <= m:
        
            temp.append(arr[left])
        
            left += 1
            
        while right <= r:
        
            temp.append(arr[right])
        
            right += 1
        
        for i in range(l, r + 1):
        
            arr[i] = temp[i - l]

        return 
            
    def mergeSort(self, arr, l, r):
        
        if l >= r:
        
            return
        
        m = (l + r) // 2
        
        self.mergeSort(arr, l, m)
        
        self.mergeSort(arr, m + 1, r)
        
        self.merge(arr, l, m, r)
        
        return



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends