from collections import deque

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        origRow = len(mat)
        origCol = len(mat[0])

        if r * c != origRow * origCol:
            return mat  # Reshape not possible

        newMat = []
        for _ in range(r):
            newMat.append([])

        items = 0
        for i in range(origRow):
            for j in range(origCol):
                row = (items)//c
                items += 1
                newMat[row].append(mat[i][j])

        return newMat
