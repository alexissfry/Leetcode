class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        top = 0

        while left <= right and top <= bottom:
            l = left 
            while l <= right: 
                result.append(matrix[top][l])
                l += 1
            top += 1

            t = top
            while t <= bottom:
                result.append(matrix[t][right])
                t += 1 
            right -= 1
        
            r = right 
            while r >= left and top <= bottom:
                result.append(matrix[bottom][r])
                r -= 1 
            bottom -= 1 
            
            b = bottom 
            while b >= top and left <= right:
                result.append(matrix[b][left])
                b -= 1 
            left += 1 

        return result 
                        
        