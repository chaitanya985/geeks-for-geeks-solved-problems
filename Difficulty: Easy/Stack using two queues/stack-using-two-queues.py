#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue 

queue_1=Queue()

queue_2=Queue()
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    
    queue_2.put(x)
    
    while not queue_1.empty():
        
        queue_2.put(queue_1.get())
        
    queue_1, queue_2=queue_2, queue_1


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    
    if queue_1.empty():
        
        return -1
        
    return queue_1.get()
    
    


#{ 
 # Driver Code Starts

from queue import Queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        queue_1 = Queue() # first queue
        queue_2 = Queue() # second queue
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1
            
        print()
        print("~")
# } Driver Code Ends