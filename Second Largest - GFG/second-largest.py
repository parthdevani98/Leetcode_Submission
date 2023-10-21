#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		largest = arr[0]
		s_largest = -1
		
		for i in range(n):
		    if arr[i] > largest:
		        s_largest = largest
		        largest = arr[i]
		    elif arr[i] < largest and arr[i] > s_largest:
		        s_largest = arr[i]
		return s_largest
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends