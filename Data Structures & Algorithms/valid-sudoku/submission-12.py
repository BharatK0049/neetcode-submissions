class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Resolve
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for row in range(9):
            for col in range(9):
                # If box is empty
                if board[row][col] == ".":
                    continue
                
                # If number in box is duplicate w.r.t row, column or particular square
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in sqrs[(row//3, col//3)]:
                    return False
                
                # Adding unseen number to row, col and square 
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sqrs[(row//3, col//3)].add(board[row][col])
        
        return True