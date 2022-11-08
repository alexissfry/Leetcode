class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        maxLen = 0

        for c in s:
            place = sub.find(c)
            if place != -1:
                sub = sub[place+1:] + c
            else:
                sub += c
                length = len(sub)
                if length > maxLen:
                    maxLen = length

        return maxLen