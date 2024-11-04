#User function Template for python3
'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''


class Solution:
    def splitList(self, head):
        #code here
        
        slow = head
        
        fast = head.next
        
        while fast != head and fast.next != head:
        
            fast = fast.next.next
        
            slow = slow.next

        h1 = head

        h2 =slow.next

        slow.next = h1
        
        curr = h2
        
        while curr.next != head:

            curr = curr.next
        
        curr.next = h2
        
        return h1,h2



#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is not None:
        temp = head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == head:
                break
        print()


def newNode(key):
    temp = Node(key)
    return temp


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        if not arr:
            continue
        head = Node(arr[0])
        temp = head
        for number in arr[1:]:
            temp.next = Node(number)
            temp = temp.next
        temp.next = head
        ob = Solution()
        head1, head2 = ob.splitList(head)
        printList(head1)
        printList(head2)
        print("~")
# } Driver Code Ends