#User function Template for python3
from collections import deque

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        
        n = len(mat)
        
        m = len(mat[0])
        
        head = Node(mat[0][0])
        
        q = deque([(0, 0, head)])
        
        while q:
        
            r, c, curr = q.popleft()
        
            if r+1<n:
        
                newNode = Node(mat[r+1][c])
        
                q.append((r+1, c, newNode))
        
                curr.down = newNode
        
            if c+1<m:
        
                newNode = Node(mat[r][c+1])
        
                curr.right = newNode
        
                q.append((r, c+1, newNode))
        
        return head


#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends