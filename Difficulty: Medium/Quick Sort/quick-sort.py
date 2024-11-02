#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        
        if low < high:
            
            indx=self.partition(arr, low, high)
            
            self.quickSort(arr, low, indx-1)
            
            self.quickSort(arr, indx+1, high)
    
    def partition(self,arr,low,high):
        # code here
        
        pivot=arr[low]
        
        left=low
        
        right=high
        
        while left < right:
            
            while arr[left] <= pivot and left <= high-1:
                
                left+=1
                
            while arr[right] >= pivot and right >= low+1:
                
                right-=1
                
            if left < right:
                
                arr[left], arr[right]=arr[right], arr[left]
                
        arr[low], arr[right]=arr[right], arr[low]
        
        return right
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

        print("~")
# } Driver Code Ends