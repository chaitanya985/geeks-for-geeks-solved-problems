#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data   
        self.next = None
'''
        
class Solution:
    def fractional_node(self, head, k):
        # Code here
        
        curr=head
        
        n=0
        
        while curr:
            
            n+=1
            
            curr=curr.next
            
        index=(n+k-1)//k
        
        curr=head
        
        count=1
        
        while curr:
        
            if index==count:
                
                return curr.data
                
            count+=1
            
            curr=curr.next
                
        return None
            
            



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        res = ob.fractional_node(head, k)
        print(res)
        index += 2

# } Driver Code Ends