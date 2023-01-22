class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origCol = image[sr][sc]
        numRows = len(image)
        numCols = len(image[0])

        def dfs(row, col):
            image[row][col] = color
            
            if 0 <= row-1 < numRows and 0 <= col < numCols and image[row-1][col] == origCol:
                dfs(row-1, col)

            if 0 <= row+1 < numRows and 0 <= col < numCols and image[row+1][col] == origCol:
                dfs(row+1, col)

            if 0 <= row < numRows and 0 <= col-1 < numCols and image[row][col-1] == origCol:
                dfs(row, col-1)

            if 0 <= row < numRows and 0 <= col+1 < numCols and image[row][col+1] == origCol:
                dfs(row, col+1)

        if origCol != color:
            dfs(sr,sc)

        return image
            
        