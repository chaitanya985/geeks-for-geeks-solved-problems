#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def checktree(self, preorder, inorder, postorder, N): 
        # Your code goes here
        
        if N == 0:
    
            return True
        
        if preorder[0] != postorder[-1]:
    
            return False
            
        if N == 1:
    
            if preorder[0] == postorder[0] and preorder[0] == inorder[0]:
    
                return True
    
            return False
            
        if len(set(preorder).union(set(inorder)).union(set(postorder))) != N:
    
            return False 
            
        
        root_idx = inorder.index(preorder[0])
        
        left_len = root_idx
        
        left_check = True
        
        if left_len > 0:
        
            left_pre = preorder[1:left_len+1]
        
            left_in = inorder[:left_len]
        
            left_post = postorder[:left_len]
            
            left_check = self.checktree(left_pre, left_in, left_post, left_len)
        
        right_len = N - root_idx - 1
        
        right_check = True
        
        if right_len > 0:
        
            right_pre = preorder[N-right_len:]
        
            right_in = inorder[N-right_len:]
        
            right_post = postorder[N-right_len-1:N-1]
            
            right_check = self.checktree(right_pre, right_in, right_post, right_len)
        
        return left_check and right_check


#{ 
 # Driver Code Starts.

# Driver Code 
if __name__ == "__main__": 
	t = int(input())
	for _ in range(t):
		n = int(input())
		preorder = list(map(int, input().strip().split()))
		inorder = list(map(int, input().strip().split()))
		postorder = list(map(int, input().strip().split()))
		obj = Solution()
		if(obj.checktree(preorder, inorder, postorder, n)):
			print("Yes") 
		else: 
			print("No") 


# } Driver Code Ends