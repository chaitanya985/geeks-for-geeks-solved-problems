#User function Template for python3


class Solution:
    
    def sol(self, output, s, res):
        
        if len(s)==0:
            
            res.append(output)
            
            return
        
        opt1=output + " " + s[0]
        
        opt2=output + s[0]
        
        s=s[1:]
        
        self.sol(opt1, s, res)
        
        self.sol(opt2, s, res)
        

    def permutation(self, s):
        # code here
        res=[]
        
        output=s[0]
        
        s=s[1:]
        
        self.sol(output, s, res)
        
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        S = input()
        ans = ob.permutation(S)
        write = ""
        for i in ans:
            write += "(" + i + ")"
        print(write)

        print("~")
# } Driver Code Ends