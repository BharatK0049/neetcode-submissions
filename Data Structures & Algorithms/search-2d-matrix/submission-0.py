class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_rows = len(matrix)
        len_cols = len(matrix[0])

        for i in range(len_rows):
            for j in range(len_cols):
                if target == matrix[i][j]:
                    return True
        
        return False