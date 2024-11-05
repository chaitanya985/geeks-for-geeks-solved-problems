#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to merge two sorted linked list.
    def sortedMerge(self,head1, head2):
        # code here
        
        res=0
        
        if head1 is None:
            
            return head2
            
        elif head2 is None:
            
            return head1
            
        if head1.data <= head2.data:
            
            res=head1
            
            res.next=self.sortedMerge(head1.next, head2)
            
        else:
            
            res=head2
            
            res.next=self.sortedMerge(head1, head2.next)
            
        return res


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = list(map(int, input().split()))
        input2 = list(map(int, input().split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends