# 53. Maximum Subarray / 最大子数组和
# 难度：中等    语言：Python3    日期：2026-10-25
# 链接：https://leetcode.cn/problems/maximum-subarray/
# 思路：动态规划（Kadane 算法）。cur_sum 表示「以当前元素结尾的最大子数组和」：
#       走到新元素时，要么自己另起一段（num），要么接在前面那段后面（cur_sum + num），取大的；
#       max_sum 记录一路见过的最大值。注意数组全是负数时答案应是其中最大那个（不能初始化成 0）。
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
