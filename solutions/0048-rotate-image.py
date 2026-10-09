# 48. Rotate Image / 旋转图像
# 难度：中等    语言：Python3    日期：2026-10-10
# 链接：https://leetcode.cn/problems/rotate-image/
# 思路：原地两步走。顺时针旋转 90° = 先沿主对角线转置（交换 matrix[i][j] 和 matrix[j][i]，
#       只遍历上三角），再把每一行 reverse。
# 复杂度：时间 O(n²)，空间 O(1)


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
