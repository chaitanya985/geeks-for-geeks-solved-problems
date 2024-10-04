#User function Template for python3

class MyQueue:
    
    def __init__(self):
        
        self.res=[]
    
    #Function to push an element x in a queue.
    def push(self, x):
    
         #add code here
        return self.res.append(x) 
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
         
         # add code here
        if len(self.res) != 0:
             
            return self.res.pop(0)
            
        else:
            
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends