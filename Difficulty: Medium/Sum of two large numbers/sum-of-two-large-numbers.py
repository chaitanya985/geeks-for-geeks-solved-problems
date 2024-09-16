#User function Template for python3
class Solution:
	def findSum(self, X, Y):
		# code here
		
		num1=int(X)
		
		num2=int(Y)
		
		return num1+num2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x = input()
		y = input()
		ob = Solution()	
		answer = ob.findSum(x,y)
		
		print(answer)


# } Driver Code Ends