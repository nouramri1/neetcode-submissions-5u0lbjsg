class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # how to make sure that we are not revisiting the same path 
        # how to figure this out ?
        dp = [[0]*(n+1) for _ in range(m+1)]
        # start from grid[m-1][n-1]
        # then check if there is an upward positio or a position to the left 
        # if so add 1 in each of those positions 
        # then keep on incrementing 
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j+1]
        return dp[0][0]

        