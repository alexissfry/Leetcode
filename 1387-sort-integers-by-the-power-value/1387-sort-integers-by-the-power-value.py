class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def getPower(x):
            if x == 1:
                return 0
            elif x%2 == 0:
                return getPower(x/2) + 1
            return getPower(3*x+1) + 1
        
        result = []
        for i in range(lo, hi+1):
            result.append((getPower(i),i))

        result.sort()

        return result[k-1][1]

'''
lo = 10, hi = 12, k = 1
result = [(6,10), (14,11), (9,12)] --> [(6,10), (9,12), (14,11)]
return 10
'''