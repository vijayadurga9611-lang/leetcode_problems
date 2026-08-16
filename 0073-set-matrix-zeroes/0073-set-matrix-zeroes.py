class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # Check if the first row has a zero
        first_row_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if the first column has a zero
        first_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Finally, handle the first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Finally, handle the first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0