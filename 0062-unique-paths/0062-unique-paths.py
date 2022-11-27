class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: # if there is one column or one row, there is only one path
            return 1
        return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1) # you can come from above (m-1) or the left (n-1)