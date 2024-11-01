#User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr): 
        # Code here
        
        first=-1
        
        last=-1
        
        for i in range(len(arr)):
            
            if arr[i]==x:
                
                if first==-1:
                    
                    first=i
                    
                last=i
                
        if first==-1:
            
            return [-1]
            
        return [first, last]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        ans = ob.firstAndLast(x, arr)
        s = (" ").join(map(str, ans))
        print(s)
        print("~")

# } Driver Code Ends