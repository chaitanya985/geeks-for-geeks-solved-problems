#User function Template for python3

class Solution:
    def subLinkedList(self, head1, head2): 
        # Code here
        # return head of difference list
        def to_num(head):
            
            num = 0
            
            while head:
            
                num = num * 10 + head.data
            
                head = head.next
            
            return num
        
        d = abs(to_num(head1) - to_num(head2))
    
        head = Node(int(str(d)[0]))
    
        curr = head
    
        for i in str(d)[1:]:
    
            curr.next = Node(int(i))
    
            curr = curr.next
    
        return head



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def print_list(head):
    """Prints the linked list."""
    while head:
        print(head.data, end='')
        head = head.next
    print()


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])
    index = 1
    solution = Solution()

    for _ in range(T):
        input1 = data[index]
        input2 = data[index + 1]
        index += 2

        head1, tail1 = None, None
        head2, tail2 = None, None

        # Create the linked list for input1
        for ch in input1:
            tmp = int(ch)
            new_node = Node(tmp)
            if head1 is None:
                head1 = new_node
                tail1 = new_node
            else:
                tail1.next = new_node
                tail1 = new_node

        # Create the linked list for input2
        for ch in input2:
            tmp = int(ch)
            new_node = Node(tmp)
            if head2 is None:
                head2 = new_node
                tail2 = new_node
            else:
                tail2.next = new_node
                tail2 = new_node

        result = solution.subLinkedList(head1, head2)
        print_list(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends