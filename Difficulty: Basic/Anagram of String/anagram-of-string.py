# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
from collections import Counter

def remAnagram(str1,str2):
    
    #add code here
    
    a=Counter(str1)
    
    b=Counter(str2)
    
    c=(a-b) + (b-a)
    
    return sum(c.values())
    
    


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends