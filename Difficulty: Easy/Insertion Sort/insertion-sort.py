#Sort the array using insertion sort

class Solution:
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        
        for i in range(0, n-1):
            
            for j in range(i+1, 0, -1):
                
                if alist[j-1] > alist[j]:
                    
                    temp=alist[j]
                    
                    alist[j]=alist[j-1]
                    
                    alist[j-1]=temp


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        Solution().insertionSort(arr, n)

        for i in range(n):
            print(arr[i], end=" ")

        print()

# } Driver Code Ends