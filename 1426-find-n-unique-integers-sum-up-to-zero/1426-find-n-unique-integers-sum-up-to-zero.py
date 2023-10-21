class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0]*n

        if n == 1:
            return [0]

        middle = n//2
        if n%2 == 1:
            right = middle + 1
            left = middle - 1
        else:
            left= middle - 1
            right= middle  

        counter = 1
        while left >= 0 and right < n:
            result[left] = counter * -1
            result[right] = counter
            counter += 1 
            left -= 1
            right += 1 

        return result

'''
edgecases: n=1

n=5 
result=[0,0,0,0,0] --> [-2,-1,0,1,2]

n=4
result=[0,0,0,0] --> [-2,-1,1,2]

n = 3
result = [0,0,0] --> [-1,0,1]
middle = 1 --> left = 0, right = 2 --> [-1,0,1]

'''