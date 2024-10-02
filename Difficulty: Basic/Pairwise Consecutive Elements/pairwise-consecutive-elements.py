#User function Template for python3

# Function to check if elements are 
# pairwise consecutive in stack 
def pairWiseConsecutive(l):
    
    #add code here
    
    arr=l
    
    if len(l)==1:
        
        return True
        
    else:
        
        for i in range(len(l)-1):
            
            if arr[i+1]==arr[i]-1 or arr[i+1]==arr[i]+1:
                
                ans=True
                
            else:
                
                ans=False
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        if(pairWiseConsecutive(l)==True):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends