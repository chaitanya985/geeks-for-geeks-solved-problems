#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
		
		arr=[]
		
		i=0
		
		stack=[]
		
		for char in str:
		    
		    if char=='(':
		        
		        i+=1
		        
		        arr.append(i)
		        
		        stack.append(i)
		        
		    elif char==')':
		        
		        arr.append(stack.pop())
		        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends