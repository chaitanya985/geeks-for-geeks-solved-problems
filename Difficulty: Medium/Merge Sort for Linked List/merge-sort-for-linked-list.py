#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        # code here
        
        temp=head
        
        arr=[]
        
        while temp is not None:
            
            arr.append(temp.data)
            
            temp=temp.next
            
        arr=sorted(arr)
        
        p1=head
        
        i=0
        
        while p1 and i < len(arr):
            
            p1.data=arr[i]
            
            i+=1
            
            p1=p1.next
            
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().mergeSort(head))
        print("~")
# } Driver Code Ends