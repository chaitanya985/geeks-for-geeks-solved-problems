#User function Template for python3

def radixSort(arr, n):
    # code here
    
    return arr.sort()


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        radixSort(arr, n)
        for ele in arr:
            print(ele, end=" ")
        print()
        t = t-1

# } Driver Code Ends