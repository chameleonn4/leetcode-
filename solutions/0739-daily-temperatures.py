# 739. Daily Temperatures / 每日温度
# 难度：中等    语言：Python3    日期：2026-10-25
# 链接：https://leetcode.cn/problems/daily-temperatures/
# 思路：单调递减栈。栈里存「还没找到更高温度」的下标，且这些下标对应的温度从栈底到栈顶单调不增。
#       遍历到 i 时，若当前温度比栈顶下标对应的温度高，说明栈顶那天的答案就是 i - 栈顶下标，弹出并记录；
#       重复这个过程直到栈空或栈顶温度 >= 当前温度，再把 i 入栈。遍历结束后仍在栈中的日子没有更高温度，记 0。
# 复杂度：时间 O(n)（每个下标最多入栈出栈各一次），空间 O(n)


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res
