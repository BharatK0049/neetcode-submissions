class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Duplicate check in rows
        for i in range(9):
            row_check = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_check:
                    return False
                row_check.add(board[i][j])
                    
        
        # Duplicate check in columns
        for i in range(9):
            column_check = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue                
                if board[j][i] in column_check:
                    return False
                column_check.add(board[j][i])
        
        # Duplicate check in squares
        for i in range(9):
            square_check = set()
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in square_check:
                        return False
                    square_check.add(board[row][col])
        return True
