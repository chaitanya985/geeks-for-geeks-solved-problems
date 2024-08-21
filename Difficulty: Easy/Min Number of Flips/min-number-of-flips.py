#User function Template for python3


class Solution:
    def minFlips(self, S):
        # Code here
        
        count=0
        
        for i in range(len(S)):
            
            if i%2==1:
                
                if S[i]=="0":
                    
                    count+=1
                    
                else:
                    continue
                
            else:
                if S[i]=="1":
                    
                    count+=1
                    
                else:
                    continue
                
        return min(count, len(S)-count)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends