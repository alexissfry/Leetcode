class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def start(left, right):
            while left <= right:
                pivot = (right + left)//2

                if nums[pivot] == target and (pivot == 0 or nums[pivot-1] < target):
                    return pivot 
                elif nums[pivot] < target:
                    left = pivot+1
                else:
                    right = pivot-1
            return -1

        def end(left, right):
            while left <= right:
                pivot = (right + left)//2

                if nums[pivot] == target and (pivot == len(nums)-1 or nums[pivot+1] > target):
                    return pivot 
                elif nums[pivot] <= target:
                    left = pivot+1
                else:
                    right = pivot-1
            return -1

        upper = len(nums)-1

        startIndex = start(0, upper)
        endIndex = end(0, upper)

        return [startIndex, endIndex]

'''
nums = [5,7,7,8,8,10], target = 8
startIndex(0,6) = 3
endIndex(0,6) = 4
return [3,4]
- 
nums = [], target = 0
startIndex(0,0)
endIndex(0,0)
–
nums = [1], target = 10
startIndex(0,1)
'''

        