class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force O(N^2)
        for i in matrix:
            if target in i:
                return True
        
        return False