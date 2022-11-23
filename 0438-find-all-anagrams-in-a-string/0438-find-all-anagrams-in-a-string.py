class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if m > n: # if p is bigger than s there can be no anagrams
            return []
        pCount = Counter(p) # count of every letter in p
        left,right = 0,m # left and right indices of our sliding window
        sCount = Counter(s[left:right]) # sliding window counter in s

        ans = [] # answer array
        while right < n: # while our sliding window is in-bounds
            if sCount == pCount: # if our counters are the same then we have found an anagram
                ans.append(left) # add the starting index of our sliding window
            sCount = sCount + Counter(s[right]) - Counter(s[left]) # add the next element, remove the last element
            right += 1 # increment forwards
            left += 1 # increment forwards 
        if sCount == pCount: # check the final sliding window
            ans.append(left)
        return ans