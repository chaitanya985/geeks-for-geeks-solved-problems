#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def insertionSort(self, head):
        #code here
        
        dummy=Node(0)
        
        curr=head
        
        while curr:
        
            prev=dummy
            
            while prev.next and prev.next.data < curr.data:
                
                prev=prev.next
                
            Next=curr.next
            
            curr.next=prev.next
            
            prev.next=curr
            
            curr=Next
                
        return dummy.next
            
            


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

        printList(Solution().insertionSort(head))

# } Driver Code Ends