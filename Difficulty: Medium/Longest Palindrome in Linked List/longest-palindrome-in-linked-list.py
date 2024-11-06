# your task is to complete this function
# function should return an integer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
class Solution:
    def maxPalindrome(self,head):
        # Code here
    
        def countcommon(a,b):
            
            count=0
            
            while a is not None and b is not None:
            
                if a.data==b.data:
            
                    count+=1
            
                else:
                    
                    break
                
                a=a.next
                
                b=b.next
                
            return count
            
        result=0
        
        prev=None
        
        curr=head
        
        while curr is not None:
        
            next_node=curr.next
        
            curr.next=prev
        
            result=max(result,2*countcommon(prev,next_node)+1)
        
            result=max(result,2*countcommon(curr,next_node))
        
            prev=curr
            
            curr=next_node
            
        return result



#{ 
 # Driver Code Starts
# Node Class
class node:

    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()

        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        obj = Solution()
        print(obj.maxPalindrome(list1.head))
        print("~")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends