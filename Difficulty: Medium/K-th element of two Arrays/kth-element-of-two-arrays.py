#User function Template for python3

def kthElement(arr1, arr2, k):
    
        merged=[]
        
        i, j=0, 0
        
        while len(merged) < k:
            
            if i < len(arr1) and (j >= len(arr2) or arr1[i] < arr2[j]):
                
                merged.append(arr1[i])
                
                i+=1
                
            else:
                merged.append(arr2[j])
                
                j+=1
                
        return merged[-1]

class Solution:
    
    def kthElement(self, k, arr1, arr2):
        
        return kthElement(arr1, arr2, k)
                
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends