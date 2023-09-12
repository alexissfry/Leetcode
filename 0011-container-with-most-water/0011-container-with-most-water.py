class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0

        while left < right:
            minSide = min(height[left],height[right])
            maxWater = max(maxWater, minSide*(right-left))
            print(minSide, maxWater)
            if minSide == height[left]:
                left += 1 
            else:
                right -= 1 

        return maxWater