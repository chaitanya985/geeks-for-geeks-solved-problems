#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        # Code here
        
        if not head:
            
            return True
            
        if not head.next:
            
            return False
            
        if head.next==head:
            
            return True
            
        fast=head.next
        
        slow=head
        
        while fast and fast.next:
            
            fast=fast.next.next
            
            slow=slow.next
            
            if slow==fast:
                
                return True
                
        return False



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Driver program to test above function
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        k = int(input().strip())
        input_line = input().strip()
        input_array = list(map(int, input_line.split()))

        head = None
        if input_array:
            head = Node(input_array[0])
            tail = head

            for x in input_array[1:]:
                tail.next = Node(x)
                tail = tail.next

            if k == 1 and head:
                tail.next = head
        ob = Solution()
        print("true" if ob.isCircular(head) else "false")
        print("~")

# } Driver Code Ends