class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        dp = [[0]*i for i in range(1,len(arr)+1)]
        dp[0][0] = arr[0][0]

        for i in range(1,len(arr)):
            for j in range(len(arr[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + arr[i][j]
                elif j == len(arr[i])-1:
                    dp[i][j] = dp[i-1][j-1] + arr[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

        minSum = float("inf")
        lastRow = len(dp)-1
        for m in range(len(dp[lastRow])):
            minSum = min(minSum, dp[lastRow][m])

        return minSum