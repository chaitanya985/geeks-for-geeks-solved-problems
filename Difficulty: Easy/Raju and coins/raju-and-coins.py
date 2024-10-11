#User function Template for python3

class Solution:
    def maxNumbers(self, n, k, a):
        # code here
        
        a.sort()
        
        i=0
        
        summ=0
        
        num=1
        
        cnt=0
        
        while summ+num<=k:
        
            if(i<n and a[i]==num):
        
                i+=1
        
            else:
        
                summ+=num
        
                cnt+=1
        
            num+=1
        
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = input().split()
        for it in range(n):
            a[it] = int(a[it])
        
        ob = Solution()
        print(ob.maxNumbers(n, k, a))
# } Driver Code Ends