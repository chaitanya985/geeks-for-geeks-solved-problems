#User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        n=len(car)
        
        res=0
        
        for i in range(n):
            
            if car[i] % 2 == 0 and date % 2 != 0:
                
                res+=fine[i]
                
            elif car[i] % 2 != 0 and date % 2 == 0:
                
                res+=fine[i]
                
        return res
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        date = int(input())
        car = [int(x) for x in input().strip().split()]
        fine = [int(x) for x in input().strip().split()]

        print(Solution().totalFine(date, car, fine))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends