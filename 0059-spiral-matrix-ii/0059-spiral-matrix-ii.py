class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        top = left = 0
        bottom = right = n - 1
        i = 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res[top][col] = i
                i += 1
            top += 1
            for row in range(top, bottom + 1):
                res[row][right] = i
                i += 1
            right -= 1
            for col in range(right, left-1, -1):
                res[bottom][col] = i
                i += 1
            bottom -= 1
            for row in range(bottom, top-1, -1):
                res[row][left] = i
                i += 1
            left += 1
        return res
        