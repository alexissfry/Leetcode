class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        numbers = [2,7,11,15] 
        complements = {7:0} --> return [1,2]
        '''

        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1 