#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        #Write your code here
        
        count1=0
        
        count0=0
        
        n=len(str)
        
        sub=0
        
        for i in range(n):
            
            if str[i]=="0":
                
                count0+=1
                
            else:
                count1+=1
                
            if count0==count1:
                
                sub+=1
                
        if count0 != count1:
            
            return -1
            
        return sub




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends