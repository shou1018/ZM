class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        for i in range(m):
            if matrix[i][n-1] >= target:
                break
        for j in range(n):
                if matrix[i][j] == target:
                    return True
                    break
        return False
