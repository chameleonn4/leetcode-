# 70. Climbing Stairs / 爬楼梯
# 难度：简单    语言：Python3    日期：2026-10-29
# 链接：https://leetcode.cn/problems/climbing-stairs/
# 思路：动态规划，本质是斐波那契。到第 i 阶的最后一步要么从 i-1 跨 1 阶上来，
#       要么从 i-2 跨 2 阶上来，所以 dp[i] = dp[i-1] + dp[i-2]。
#       边界：dp[0] = 1（站在地面算一种）、dp[1] = 1（只能跨 1 阶）。
#       注意 n = 1 时循环不执行，直接返回 dp[1]，不会越界。
# 复杂度：时间 O(n)，空间 O(n)（可滚动优化到 O(1)）


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
