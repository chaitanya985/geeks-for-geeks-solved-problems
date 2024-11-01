#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        
        temp={}
        
        c=0
        
        for i in arr:
            
            if i in temp:
                
                temp[i]+=1
                
            else:
                temp[i]=1
                
        occur=n//k
        
        for count in temp.values():
            
            if count > occur:
                
                c+=1
                
        return c
            
            
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


            print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends