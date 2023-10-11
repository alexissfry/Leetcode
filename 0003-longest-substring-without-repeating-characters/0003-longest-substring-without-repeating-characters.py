class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        left = 0
        right = 0
        maxLen = 0

        while right < len(s):
            r = s[right]
            chars[r] += 1 

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1 
                left += 1 

            maxLen = max(maxLen, right-left+1)
            right += 1 

        return maxLen 


'''
abccd --> abc


'''