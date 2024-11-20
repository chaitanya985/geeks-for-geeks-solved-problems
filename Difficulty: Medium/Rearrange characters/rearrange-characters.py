#User function Template for python3
from collections import Counter

class Solution :
    def rearrangeString(self, s):
        #code here
        count = Counter(s)
        
        max_count = max(count.values())
        
        if max_count > (len(s) + 1) // 2:
        
            return "-1"
        
        result = [''] * len(s)
        
        idx = 0
        
        for char, freq in count.most_common():
        
            for _ in range(freq):
        
                result[idx] = char
        
                idx += 2
        
                if idx >= len(s):
        
                    idx = 1
        
        return ''.join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=='-1':
            print(0)
        elif sorted(str1)!=sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i]==str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
        
        print("~")
# } Driver Code Ends