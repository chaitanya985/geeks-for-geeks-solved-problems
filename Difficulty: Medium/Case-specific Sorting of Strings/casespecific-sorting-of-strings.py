#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        
        lower_char=sorted([ch for ch in s if ch.islower()])
        
        upper_char=sorted([ch for ch in s if ch.isupper()])
        
        result=[]
        
        lower_index=0
        
        upper_index=0
        
        for ch in s:
            
            if ch.islower():
                
                result.append(lower_char[lower_index])
                
                lower_index+=1
                
            else:
                
                result.append(upper_char[upper_index])
                
                upper_index+=1
                
        return ''.join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends