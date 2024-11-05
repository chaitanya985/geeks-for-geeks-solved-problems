#User function Template for python3

'''
# Linked List Node 
class Node: 
	def __init__(self, d): 
		self.data = d 
		self.next = None
		'''
class Solution:    
    def rearrangeEvenOdd(self, head):
        #code here
        
        ptr=head
        
        curr=head.next
        
        k=curr
        
        while(ptr.next != None and curr.next != None):
            
            ptr.next=curr.next
            
            ptr=curr.next
            
            curr.next=ptr.next
            
            curr=ptr.next
            
        ptr.next=k
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        Solution().rearrangeEvenOdd(head)
        printList(head)

# This code is contributed by Prerna Saini

# } Driver Code Ends