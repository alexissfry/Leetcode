class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0
        
        while left < right:
            water = min(height[left],height[right])*(right-left)
            if water > maxWater:
                maxWater = water
                
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxWater