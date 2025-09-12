class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        result = [[1], [1, 1]]

        for i in range(2, numRows):
            newRow = [1, 1]
            for j in range(1, i):
                newRow.insert(j, result[-1][j - 1] + result[-1][j])
            result.append(newRow)
        return result
    