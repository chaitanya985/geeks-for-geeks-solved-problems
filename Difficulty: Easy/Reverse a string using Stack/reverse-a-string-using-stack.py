#{ 
 # Driver Code Starts

# } Driver Code Ends

def createStack(): return []

def size(stack): return len(stack)

def isEmpty(stack): return size(stack) == 0

def push(stack, item): stack.append(item)

def pop(stack): return stack.pop() if not isEmpty(stack) else None

def reverse(string):

    stack = createStack()

    for char in string: push(stack, char)

    return ''.join(pop(stack) for _ in range(size(stack)))
   

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends