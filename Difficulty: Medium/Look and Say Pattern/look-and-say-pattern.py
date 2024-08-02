#User function Template for python3

class Solution:

    def lookandsay(self, n):
        # code here
        
        if n==1:
            
            return "1"
            
        prev=self.lookandsay(n-1)
        
        result=""
        
        count=1
        
        for i in range(len(prev)):
            
            if i+1 < len(prev) and prev[i] == prev[i+1]:
                
                count+=1
                
            else:
                result += str(count) + prev[i]
                
                count=1
                
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends