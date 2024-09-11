#User function template for Python

class Solution:
    def remove_duplicate(self, arr):
        #Code Here
        l=1
        
        for i in range(1, len(arr)):
            
            if arr[i] != arr[i-1]:
                
                arr[l]=arr[i]
                
                l+=1
                
            else:
                continue
            
        return l


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.remove_duplicate(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()

# } Driver Code Ends