#User function Template for python3
from collections import deque

from heapq import heapify, heappush, heappop 

class Solution:

        def find_range(self,d):
        
            heap = []
        
            heapify(heap)
            
            maxi = -1e9
            
            ans = (-1e9,1e9)
            
            for i in d:
            
                heappush(heap,(d[i][0],i,0))
            
                maxi = max(maxi,d[i][0])
            
            while True:
            
                poped,i,j = heappop(heap)
            
                if maxi - poped < ans[1] - ans[0]:
            
                    ans = (poped,maxi)
            
                if j+1 >= len(d[i]):
            
                    break
            
                maxi = max(maxi,d[i][j+1])
                
                heappush(heap,(d[i][j+1],i,j+1))
        
            return ans
        
        def shortestRange(self, root):
    
            d = {}
            
            stack = deque()
            
            stack.append((root,0))
            
            while stack:
            
                poped,level = stack.popleft()
            
                if level not in d:
            
                    d[level] = []
            
                d[level].append(poped.data)
            
                if poped.left:
            
                    stack.append((poped.left,level+1))
            
                if poped.right:
            
                    stack.append((poped.right,level+1))
            ans = self.find_range(d)
            
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    from collections import deque
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        ans = obj.shortestRange(root)
        print(ans[0],ans[1])



# } Driver Code Ends