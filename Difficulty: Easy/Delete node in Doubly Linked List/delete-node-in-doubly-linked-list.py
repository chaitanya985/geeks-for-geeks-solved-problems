class Solution:
    def delete_node(self, head, x):
        #code here
        
        if not head:
            
            return None
            
        if x==1:
            
            head=head.next
            
            if head:
                
                head.prev=None
                
            return head
            
        curr=head
        
        count=1
        
        while curr and count < x:
            
            curr=curr.next
            
            count+=1
            
        if not curr:
            
            return head
            
        if curr.prev:
            
            curr.prev.next=curr.next
            
        if curr.next:
            
            curr.next.prev=curr.prev
            
        return head


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = Node(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def printList(head):
    if not head:
        return

    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.delete_node(head, int(input().strip()))
        printList(resHead)

# } Driver Code Ends