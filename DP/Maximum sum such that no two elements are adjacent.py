# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/#
# - DP: nums[i] can either be part of the res, or not
# 	- Use a n * 2 array, or 2 arrays of size n:
# 		- dp1[i]: max subsequence including nums[i]
# 			- dp1[i] = dp2[i-1] + nums[i]
# 		- dp2[i]: max subsequence not including nums[i]
# 			- dp2[i] = max(dp1[i-1], dp2[i-1]) # nums[i-1] can be negative
# 		- dp1[0] = nums[0]; dp2[0] = 0
# 		- Iterate in range(1, len(nums))

def findMaxSum(arr, N):
    # Declare dp array
    dp = [[0 for i in range(2)] for j in range(N)]

    if (N == 1):
        return arr[0]

    # Initialize the values in dp array
    dp[0][0] = 0
    dp[0][1] = arr[0]

    # Loop to find the maximum possible sum
    for i in range(1, N):
        dp[i][1] = dp[i - 1][0] + arr[i]
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])

    # Return the maximum sum
    return max(dp[N - 1][0], dp[N - 1][1])


# Driver Code

# Creating the array
arr = [5, 5, 10, 100, 10, 5]
N = len(arr)

# Function call
print(findMaxSum(arr, N))