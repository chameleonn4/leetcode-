# 55. Jump Game / 跳跃游戏
# 难度：中等    语言：Python3    日期：2026-10-28
# 链接：https://leetcode.cn/problems/jump-game/
# 思路：贪心。不用记录每个位置能不能到，只维护「目前能到达的最远下标」far。
#       遍历位置 i，若 i <= far 说明 i 可达，从 i 出发最远能到 i + nums[i]，用它更新 far。
#       循环条件里 far < n - 1 表示一旦够到终点就提前结束。
#       最后 far >= n - 1 说明能到达最后一个下标。
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        far = 0
        i = 0
        while i <= far and far < n - 1:
            far = max(far, i + nums[i])
            i += 1
        return far >= n - 1
