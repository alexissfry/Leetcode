class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            k = (l+r)//2
            coins_needed = k*(k+1)//2
            
            if coins_needed == n:
                return k
            elif coins_needed < n:
                l = k+1
            else:
                r = k-1
        
        return r