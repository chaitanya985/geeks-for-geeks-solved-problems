#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
        count={}
        
        for char in arr:
            
            count[char] = count.get(char, 0)+1
            
        first_max=second_max=-1
        
        first_char=second_char=None
        
        for key, value in count.items():
            
            if value > first_max:
                
                second_max, second_char = first_max, first_char
                
                first_max, first_char=value, key
                
            elif first_max > value > second_max:
                
                second_max, second_char = value, key
        
        return second_char if second_char else ""
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends