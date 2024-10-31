#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        
        visited=[False]*(leaves+1)
        
        strength=set(frogs)
        
        for stre in strength:
            
            for i in range(stre, leaves+1, stre):
                
                visited[i]=True
                
        unvisit=visited[1:].count(False)
        
        return unvisit


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))
        
        T -= 1
        print("~")
# } Driver Code Ends