#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        
        n=len(S)
        
        for i in range(2, n):
            
            left=0
            
            right=i
            
            while right < n:
                
                window=S[left:right+1]
                
                if "0" in window and "1" in window and "2" in window:
                    
                    return len(window)
                    
                else:
                    
                    left+=1
                    
                    right+=1
                    
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends