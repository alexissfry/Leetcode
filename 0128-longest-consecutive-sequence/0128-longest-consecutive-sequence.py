class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxCons = 0
        
        for num in nums:
            if num-1 not in numSet:
                curr = num
                currCons = 0
                while curr in numSet:
                    currCons += 1 
                    curr += 1
                maxCons = max(maxCons, currCons)
        
        return maxCons