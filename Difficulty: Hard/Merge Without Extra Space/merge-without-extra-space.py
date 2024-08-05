#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        i=n-1
        
        j=0
        
        while i>=0 and j<m:
            
            if arr1[i] > arr2[j]:
                
                arr1[i], arr2[j] = arr2[j], arr1[i]
                
                i-=1
                
                j+=1
                
            else:
                
                break
            
        arr1.sort()
        
        arr2.sort()
    



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends