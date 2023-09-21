class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i,n in enumerate(nums):
            complement = target - n 

            if complement in tracker:
                return (tracker[complement],i)
            else:
                tracker[n] = i

        return []