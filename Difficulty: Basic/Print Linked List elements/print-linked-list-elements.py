#Your task is to complete this function
#Your function should print the data in one line only

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    # Function to display the elements of a linked list
    def display(self, head):
        #code here
        
        temp=head
        
        while temp:
            
            print(temp.data,end=" ")
            
            temp=temp.next
            
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input_list = list(map(int, input().split()))
        head = None
        tail = None

        # Building the linked list from input
        for x in input_list:
            if head is None:
                head = Node(x)
                tail = head
            else:
                tail.next = Node(x)
                tail = tail.next

        ob = Solution()
        ob.display(head)
        print()  # newline after printing the linked list

# } Driver Code Ends