class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascale = []
        pascale.append([1])
        rows = 1

        while rows < numRows:
            pascale.append([1])
            for i in range(len(pascale[rows-1])-1):
                pascale[rows].append(pascale[rows-1][i] + pascale[rows-1][i+1])
            pascale[rows].append(1)
            rows += 1
            
        return pascale