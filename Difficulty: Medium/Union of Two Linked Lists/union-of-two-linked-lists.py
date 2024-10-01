#User function Template for python3

class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        
        sets=set()
        
        p1=head1
        
        p2=head2
        
        dummy=Node(None)
        
        tail=dummy
        
        while p1:
            
            sets.add(p1.data)
            
            p1=p1.next
            
        while p2:
            
            sets.add(p2.data)
            
            p2=p2.next
            
        sorted_sets=sorted(sets)
        
        for data in sorted_sets:
            
            tail.next=Node(data)
            
            tail=tail.next
            
        tail.next=None
        
        return dummy.next
            
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)

        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)

        ob = Solution()
        printList(ob.union(ll1.head, ll2.head))
        print()

# } Driver Code Ends