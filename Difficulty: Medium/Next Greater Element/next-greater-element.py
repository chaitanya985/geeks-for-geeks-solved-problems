# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        
        res=[]
        
        for i in range(len(arr)):
            
            for j in range(i+1, len(arr)):
                
                if arr[j]>arr[i]:
                    
                    res.append(arr[j])
                    
                    break
                
                if j==len(arr)-1:
                    
                    res.append(-1)
                    
        res.append(-1)
        
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends