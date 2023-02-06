class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set) #keys are going to be (r/3, c/3)
        
        c = len(board[0])
        r = len(board)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue 
                if ((board[i][j] in row[i]) or 
                   (board[i][j] in col[j]) or 
                   (board[i][j] in squares[(i//3,j//3)])):
                    return False 
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
                
        return True 