class MyStack:
    
    def __init__(self):
        
        self.head = None
    #Function to push an integer into the stack.
    def push(self, data):

        # Add code here
        Node=StackNode(data)
        
        if self.head is None:
            
            self.head=Node
            
        else:
            Node.next=self.head
            
            self.head=Node


    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if self.head is None:
            
            return -1
            
        data=self.head.data
        
        self.head=self.head.next
        
        return data



#{ 
 # Driver Code Starts
class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()

# } Driver Code Ends