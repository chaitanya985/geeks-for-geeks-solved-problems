#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def quick_sort(self, head):
        # Your code goes here
        
        lst=[]
        
        temp=head
        
        while(temp):
        
            lst.append(temp.data)
        
            temp=temp.next
        
        lst.sort()
        
        head=None
        
        if(lst==[]):
        
            return head
        
        head=DLLNode(lst[0])
        
        temp=head
        
        for i in range(1,len(lst)):
        
            temp.next=DLLNode(lst[i])
        
            temp=temp.next
        
        return head


#{ 
 # Driver Code Starts
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(head_ref, tail_ref, new_data):
    new_node = DLLNode(new_data)

    new_node.next = None

    if tail_ref[0] is not None:
        new_node.prev = tail_ref[0]
        tail_ref[0].next = new_node
    else:
        head_ref[0] = new_node
        new_node.prev = None

    tail_ref[0] = new_node


def print_list(head):
    if head is None:
        return

    while head is not None:
        print(head.data, end=" ")
        head = head.next


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        head = [None]
        tail = [None]
        for num in arr:
            push(head, tail, num)

        obj = Solution()
        head[0] = obj.quick_sort(head[0])
        print_list(head[0])
        print()

# } Driver Code Ends