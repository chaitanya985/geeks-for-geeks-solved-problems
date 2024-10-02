
class Solution:
    def removeAdj(self,arr):
        # Your code goes here
        
        list1=[]
        
        for i in range(len(arr)):
            
            if len(list1) > 0 and list1[-1] == arr[i]:
            
                list1.pop()
            
            else:
            
                list1.append(arr[i])
        
        return len(list1)
        
    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr = [x for x in input().split()]
        ob = Solution()
        print(ob.removeAdj(arr))

# } Driver Code Ends