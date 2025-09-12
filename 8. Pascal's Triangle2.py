class Solution:
    def generate(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        lastRow = [1, 1]

        for i in range(2, rowIndex+1):
            newRow = [1, 1]
            for j in range(1, i):
                newRow.insert(j, lastRow[j - 1] + lastRow[j])
            lastRow = newRow
        return lastRow

print(Solution().generate(2))