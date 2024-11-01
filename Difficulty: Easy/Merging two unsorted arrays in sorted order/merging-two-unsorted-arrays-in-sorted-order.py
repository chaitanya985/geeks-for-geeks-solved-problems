#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def sortedMerge(self, arr1,arr2,res):
        # Your code goes here
        
        list1=[]
        
        list1=list1+arr1+arr2
        
        list1.sort()
        
        for i in range(len(list1)):
            
            res[i]=list1[i]
            
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        # First line contains the sizes of the arrays
        # Split the combined list into arr1 and arr2
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        n = len(arr1)
        m = len(arr2)

        res = [0] * (n + m)  # Initialize the result array with size n + m
        ob = Solution()
        ob.sortedMerge(arr1, arr2, res)

        # Print the merged array
        for i in res:
            print(i, end=" ")
        print()
        print("~")
# } Driver Code Ends