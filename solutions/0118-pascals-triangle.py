# 118. Pascal's Triangle / 杨辉三角
# 难度：简单    语言：Python3    日期：2026-10-29
# 链接：https://leetcode.cn/problems/pascals-triangle/
# 思路：先把第 i 行开成长度 i+1 的全 0 数组，每行首尾置 1；
#       中间的每个数是它左上方和右上方之和：dp[i][j] = dp[i-1][j-1] + dp[i-1][j]。
#       因为行内从左往右填，dp[i-1] 已经算好，所以按行递推即可。
#       注意 j 从 1 开始、到 i-1 结束，首尾两个 1 不用重算。
# 复杂度：时间 O(numRows^2)，空间 O(numRows^2)（要返回整个三角形）


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * i for i in range(1, numRows + 1)]

        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1

        res = []
        for i in range(numRows):
            for j in range(i):
                if i != 0 and j != 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            res.append(dp[i])

        return res
