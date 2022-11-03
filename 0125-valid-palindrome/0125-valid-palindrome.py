class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ''.join(c for c in s if c.isalnum())
        alpha = alpha.lower()
        
        left = 0
        right = len(alpha)-1
        
        if right == -1:
            return True
        
        while left < right:
            if alpha[left] != alpha[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True