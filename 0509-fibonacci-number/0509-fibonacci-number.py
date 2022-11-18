class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        sequence = [0, 1]
        currentFib = 0
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        for i in range(2,n+1):
            print(i)
            currentFib = sequence[i-2] + sequence[i-1]
            sequence.append(currentFib)
        
        return currentFib
        