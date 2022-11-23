class Solution:
    def characterReplacement(self, s, k):
        left,right = 0,k # left and right of our sliding window
        substring = Counter(s[:k]) # we know we can have at least k elements
        maxCount = 0 # maximum count of a single element we have had in a window
        ans = k # answer is at least k

        n = len(s) 
        while right < n:
            substring[s[right]] += 1 # add the next element
            maxCount = max(maxCount, substring[s[right]]) # update the maxCount if necessary
            if ans < maxCount + k: # if we have space for another element that we can replace
                ans += 1 # increment the answer
            else:
                substring[s[left]] -= 1 # otherwise, remove the last element in our window
                left += 1 # move the end forward
            right += 1 # move forward

        return ans
        