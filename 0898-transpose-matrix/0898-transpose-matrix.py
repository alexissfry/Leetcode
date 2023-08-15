class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        newMatrix = []

        for r in range(cols):
            newMatrix.append([])

        for i in range(rows):
            for j in range(cols):
                newMatrix[j].append(matrix[i][j])
        return newMatrix