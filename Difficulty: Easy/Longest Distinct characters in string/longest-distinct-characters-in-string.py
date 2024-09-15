#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        
        seen=set()
        
        max_length=0
        
        start=0
        
        for end in range(len(S)):
            
            while S[end] in seen:
                
                seen.remove(S[start])
                
                start+=1
                
            seen.add(S[end])
            
            max_length=max(max_length, end-start+1)
            
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends