class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Optimal Solution: O(log(mn))

        rows, cols = len(matrix), len(matrix[0])
        # Defining our pointers
        left, right = 0, (rows * cols) - 1

        while left <= right:
            # Mid-point
            mid = (left + right) // 2            
            row = mid // cols
            col = mid % cols

            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
