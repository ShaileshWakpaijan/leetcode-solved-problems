# LeetCode 74

class Solution:
    def searchMatrix(self, matrix, target):
        yl, yr = 0, len(matrix)-1
        while yl <= yr:
            mid = yl + (yr - yl) // 2
            if target < matrix[mid][0]:
                yr = mid - 1
            elif target > matrix[mid][-1]:
                yl = mid + 1
            else:
                break

        if yl > yr:
            return False

        row = mid
        xl, xr = 0, len(matrix[row]) - 1
        while xl <= xr:
            mid = xl + (xr - xl) // 2
            if target < matrix[row][mid]:
                xr = mid - 1
            elif target > matrix[row][mid]:
                xl = mid + 1
            else:
                return True
        
        return False