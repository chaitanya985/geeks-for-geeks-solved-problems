from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        # code here
    
        def is_prime(num):
    
            if num < 2:
    
                return False
    
            for i in range(2, int(num ** 0.5) + 1):
    
                if num % i == 0:
    
                    return False
    
            return True

        def next_prime(num):
    
            if num == 1:
    
                return 2
    
            lower_prime = num - 1
    
            while lower_prime >= 2:
    
                if is_prime(lower_prime):
    
                    break
        
                lower_prime -= 1

            upper_prime = num + 1
        
            while True:
        
                if is_prime(upper_prime):
        
                    break
        
                upper_prime += 1

            if num - lower_prime <= upper_prime - num:
            
                return lower_prime
            
            else:
            
                return upper_prime

        temp = head
    
        while temp:
    
            if not is_prime(temp.data):
    
                num = next_prime(temp.data)
    
                temp.data = num
    
            temp = temp.next
    
        return head
        



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()


def inputList():

    data = [int(i) for i in input().strip().split()
            ]  #all data of linked list in a line
    head = Node(data[0])
    tail = head
    for i in range(1, len(data)):
        tail.next = Node(data[i])
        tail = tail.next
    return head


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        head = inputList()

        obj = Solution()
        res = obj.primeList(head)

        printList(res)

# } Driver Code Ends