#User function Template for python3



def maxArea(A,le):
    #code here
    
    if le < 2:
        
        return 0
        
    max_water=0
    
    left=0
    
    right=le-1
    
    while left < right:
        
        width=right-left
        
        height=min(A[left], A[right])
        
        max_area=width*height
        
        max_water=max(max_water, max_area)
        
        if A[left] < A[right]:
            
            left+=1
            
        else:
            right-=1
            
    return max_water
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends