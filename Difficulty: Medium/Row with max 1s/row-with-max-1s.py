class Solution:
    def rowWithMax1s(self, arr):
        # code here
        n = len(arr)
        
        m = len(arr[0])
        
        r = 0  
        
        c = m - 1  
        
        max_row_index = -1  

        while r < n and c >= 0:

            if arr[r][c] == 1:

                max_row_index = r

                c -= 1

            else:

                r += 1

        return max_row_index


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    tc = int(data[idx])
    idx += 1
    results = []

    for _ in range(tc):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        ans = Solution().rowWithMax1s(arr)
        results.append(ans)

    for result in results:
        print(result)

# } Driver Code Ends