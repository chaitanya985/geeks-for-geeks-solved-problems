class Solution:
    def findTriplet(self, arr):
        
        arr.sort()
        
        n=len(arr)
        
        left=0
        
        right=n-2
        
        num=n-1
        
        while num>0:
        
            left=0
        
            right=num-1
        
            while left<right:
        
                temp=arr[left]+arr[right]
        
                if temp==arr[num]:
        
                    return True
        
                elif temp<arr[num]:
        
                    left+=1
        
                else:
        
                    right-=1
        
            num-=1
        
        return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends