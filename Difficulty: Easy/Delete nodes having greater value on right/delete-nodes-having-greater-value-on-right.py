#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        
        node = None
        
        if(head != None):
        
            while(head != None):
        
                temp = head
        
                head = head.next
        
                temp.next = node
        
                node = temp
   
            temp = node.next
        
            prev = node
        
            while(temp != None):
        
                if(prev.data > temp.data):
        
                    prev.next = temp.next
        
                    temp = temp.next
        
                else:
        
                    prev = prev.next
        
                    temp = temp.next
                
            while(node != None):
        
                temp = node
        
                node = node.next
        
                temp.next = head
        
                head = temp
        
        else:
        
            return None
            
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3


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

    def getNode(
            self,
            value):  # return node with given value, if not present return None
        curr_node = self.head
        while (curr_node.next and curr_node.data != value):
            curr_node = curr_node.next
        if (curr_node.data == value):
            return curr_node
        else:
            return None

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


if __name__ == "__main__":
    t = int(input())
    while (t > 0):

        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)

        result = Solution().compute(a.head)
        a.head = result
        a.printList()
        t -= 1
        print("~")

# } Driver Code Ends