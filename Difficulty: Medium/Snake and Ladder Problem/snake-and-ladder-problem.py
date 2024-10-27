# User function Template for Python3

class Solution:
    def minThrow(self, N, arr):
        # code here
        
        moves = [0] * 31  
        
        for i in range(0, 2*N, 2):

            src, dest = arr[i]-1, arr[i+1]-1

            moves[src] = dest
        
        from collections import deque
        
        visited = [False] * 31
        
        q = deque([(0, 0)])  
        
        visited[0] = True
        
        while q:
            
            pos, dice_throws = q.popleft()
            
            for i in range(1, 7):
                
                next_pos = pos + i
                
                if next_pos > 30:
                
                    continue
                
                if moves[next_pos] != 0:
                    
                    next_pos = moves[next_pos]
                
                if next_pos == 29:  
                    
                    return dice_throws + 1
                
                if not visited[next_pos]:
                    
                    visited[next_pos] = True
                    
                    q.append((next_pos, dice_throws + 1))
        
        return -1 


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
        print("~")
# } Driver Code Ends