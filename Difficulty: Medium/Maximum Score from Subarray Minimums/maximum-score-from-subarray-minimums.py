#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        # Your code goes here
        
        ans=-sys.maxsize
        
        sum=0
        
        for i in range(len(arr)-1):
        
            sum=arr[i]+arr[i+1]
        
            if sum>ans:
               
                ans=sum
                
            else:
                
                sum=0
                
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends