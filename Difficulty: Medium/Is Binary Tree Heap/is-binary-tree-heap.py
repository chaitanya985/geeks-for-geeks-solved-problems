#User Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        def count(root):
            
            if root==None:
            
                return 0
            
            return 1+count(root.left)+count(root.right)
            
        def iscbt(root,idx,tot):
            
            if root==None:
            
                return True
                
            if idx>=tot:
                
                return False
            
            left=iscbt(root.left,idx*2+1,tot)
            
            right=iscbt(root.right,2*idx+2,tot)
            
            return left and right
            
        def ismax(root):
            
            if root==None:
            
                return True
            
            if root.left==None and root.right==None:
            
                return True
            
            if root.right==None:
            
                return root.data>root.left.data
            
            elif root.left==None:
            
                return False
                
            left=ismax(root.left)
            
            right=ismax(root.right)
            
            return left and right and root.data>root.left.data and root.data>root.right.data
            
        tot=count(root)

        return iscbt(root,0,tot) and ismax(root)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Susanta Mukherjee
import sys
sys.setrecursionlimit(10**6)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        ob = Solution()
        if ob.isHeap(root):
            print(1)
        else:
            print(0)
        
        

        print("~")
# } Driver Code Ends