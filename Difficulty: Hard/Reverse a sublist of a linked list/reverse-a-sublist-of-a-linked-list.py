#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverseBetween(self, a, b, head):
        #code here
        
        temp = head
        
        arr = []
        
        n = 0
        
        bn = None
        
        an = None
        
        cn = None
        
        y = None
        
        while(temp!=None):
        
            n+=1
        
            if n==a-1:
        
                an = temp
        
            if n>=a and n<=b:
        
                if cn==None:
        
                    cn = Node(temp.data)
        
                    cn.next = None
        
                    y = cn
        
                else:
        
                    x = Node(temp.data)
        
                    x.next = cn
        
                    cn = x
        
            if n==b+1:
        
                bn = temp
        
            temp = temp.next
        
        if an == None:
        
            head = cn
        
        else:
        
            an.next = cn
        
        y.next = bn
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self, head):
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        inp = list(map(int, input().split()))
        m = inp[0]
        n = inp[1]

        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)

        ob = Solution()
        newhead = ob.reverseBetween(m, n, a.head)
        a.printList(newhead)

# } Driver Code Ends