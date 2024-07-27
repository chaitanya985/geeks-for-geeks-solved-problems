class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		if not Intervals:
		    
		    return []
		    
	    Intervals.sort(key=lambda x:x[0])
	    
	    merged=[Intervals[0]]
	    
	    for current in Intervals[1:]:
	        
	        if current[0] <= merged[-1][1]:
	            
	            merged[-1][1] = max(merged[-1][1], current[1])
	            
	        else:
	            merged.append(current)
	            
        return merged
	        
	        

#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends