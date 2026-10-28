# 45. Jump Game II / 跳跃游戏 II
# 难度：中等    语言：Python3    日期：2026-10-28
# 链接：https://leetcode.cn/problems/jump-game-ii/
# 思路：贪心 + BFS 分层。end 表示「当前这一层（用 steps 步）能到达的最远位置」，
#       max_pos 表示「再跳一步能到达的最远位置」。遍历每个位置 i 更新 max_pos = max(max_pos, i + nums[i])，
#       当 i == end 时，说明当前层扫完了，必须再多跳一步：end = max_pos，steps += 1。
#       注意循环只到 len(nums) - 1（终点不需要再跳），否则会多算一步。
# 复杂度：时间 O(n)，空间 O(1)


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end, max_pos = 0, 0
        steps = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
                steps += 1
        return steps
