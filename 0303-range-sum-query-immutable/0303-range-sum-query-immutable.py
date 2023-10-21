class NumArray:

    # nums is accessible throughout the class NumArray
    def __init__(self, nums: List[int]):
        runningSum = [0]*len(nums)
        runningSum[0] = nums[0]
        for i in range(1,len(nums)):
            runningSum[i] = runningSum[i-1] + nums[i]
        self.runningSum = runningSum

    # while left <= right --> store sum and return it
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.runningSum[right]
        return self.runningSum[right] - self.runningSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)