"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def rearrange(self, head):
        # Code here
        
        t=head
        
        ans=[]
        
        while(t != None):
            
            ans.append(t.data)
            
            t=t.next
            
        ans=ans[::2]+ans[1::2][::-1]
        
        t1=head
        
        i=0
        
        while (t1 != None):
            
            t1.data=ans[i]
            
            i+=1
            
            t1=t1.next
            
        return head


#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()

        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)

        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
        print("~")
# Contributed by: Harshit Sidhwa

# } Driver Code Ends