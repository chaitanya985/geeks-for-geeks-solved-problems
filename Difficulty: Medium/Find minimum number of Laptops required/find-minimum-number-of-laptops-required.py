#User function Template for python3

class Solution: 
    def minLaptops(self, N, start, end):
        # Code here
        
        start.sort()
        
        end.sort()
        
        laptop=1
        
        i=1
        
        j=0
        
        l=[1]
        
        while (i<N and j<N):
            
            if end[j]>start[i]:
                
                laptop+=1
                
                i+=1
                
            else:
                laptop-=1
                
                j+=1
                
            l.append(laptop)
            
        return max(l)
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
            
        ob = Solution()
        print(ob.minLaptops(N, start, end))
        
        T -= 1

# } Driver Code Ends