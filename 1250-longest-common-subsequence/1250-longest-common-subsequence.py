class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Make a grid of 0s with len(text2)+1 columns and len(text1)+1 rows
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        # Iterate up each column, starting from the last one
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col]==text1[row]: #Characters are equal
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        
        return dp[0][0]
        

