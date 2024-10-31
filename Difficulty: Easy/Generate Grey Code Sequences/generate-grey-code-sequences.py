# Your task is to complete this function
# Function should return a list of all the Grey Code Generated
class Solution:
    def generateCode(self, n):
        # Code here
        
        result = []
        
        for i in range(2**n):
        
            gray = i ^ (i >> 1)
        
            result.append(bin(gray)[2:].zfill(n))
        
        return result


#{ 
 # Driver Code Starts


# Driver Program

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        res = Solution().generateCode(int(input()))
        for j in range (len (res)):
            print (res[j], end = " ") 
        print ()


        print("~")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends