#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        
        list=[]
        
        for i in range(N):
        
            if asteroids[i]>0:
        
                list.append(asteroids[i])
        
            else:
        
                while list and list[-1]>0 and list[-1]<abs(asteroids[i]):
        
                    list.pop()
        
                if list and list[-1]==abs(asteroids[i]):
        
                    list.pop()
                
                elif not list or list[-1]<0:
        
                    list.append(asteroids[i])
        
        return list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends