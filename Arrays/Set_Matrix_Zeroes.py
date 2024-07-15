class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ind = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ind.append((i, j))
        l =len(ind)
        while l:
            p = ind[0][0]
            q = ind[0][1]
            for i in range(m):
                matrix[i][q] = 0
            for i in range(n):
                matrix[p][i] = 0
            l -= 1
            ind.pop(0)
        