#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution():
#Function to sort the given doubly linked list using Merge Sort.
    def sort_doubly(self, head):
        #Your code here
        
        arr = []
        
        ptr = head
        
        while ptr:
        
            arr.append(ptr.data)
        
            ptr = ptr.next
        
        arr.sort()
        
        ptr1 = head
        
        for i in range(len(arr)):
        
            ptr1.data = arr[i]
        
            ptr1 = ptr1.next
        
        return head
    


#{ 
 # Driver Code Starts
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail_ref, new_data):
    new_node = DLLNode(new_data)
    new_node.next = None
    new_node.prev = tail_ref

    if tail_ref:
        tail_ref.next = new_node

    return new_node


def print_list(head):
    if head is None:
        return

    # Forward traversal
    result_forward = []
    last = None
    while head is not None:
        result_forward.append(str(head.data))
        last = head
        head = head.next

    print(" ".join(result_forward))

    # Backward traversal
    result_backward = []
    while last is not None:
        result_backward.append(str(last.data))
        last = last.prev

    print(" ".join(result_backward))


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        if not arr:
            print("List is empty.")
            continue

        head = DLLNode(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        obj = Solution()
        sorted_head = obj.sort_doubly(head)

        print_list(sorted_head)

# } Driver Code Ends