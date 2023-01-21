class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute force solution
        rowNums = []
        columnNums = []
        
        for rowNum in range(len(matrix)):
            for columnNum in range(len(matrix[rowNum])):
                if matrix[rowNum][columnNum] == 0:
                    rowNums.append(rowNum)
                    columnNums.append(columnNum)

        for rowNum in range(len(matrix)):
            for columnNum in range(len(matrix[rowNum])):
                if rowNum in rowNums or columnNum in columnNums:
                    matrix[rowNum][columnNum] = 0
            
