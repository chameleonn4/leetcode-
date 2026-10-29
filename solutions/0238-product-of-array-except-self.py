# 238. Product of Array Except Self / 除了自身以外数组的乘积
# 难度：中等    语言：Python3    日期：2026-10-29
# 链接：https://leetcode.cn/problems/product-of-array-except-self/
# 思路：题目禁止用除法，所以用「前缀积 × 后缀积」。两趟遍历、复用输出数组 res：
#       第一趟从左往右，res[i] 先存 i 左边所有元素的乘积（res[i] = left，然后 left *= nums[i]）；
#       第二趟从右往左，res[i] *= right，再把 right *= nums[i] 把 nums[i] 乘进 right，
#       这样 res[i] 最终 = 左边乘积 × 右边乘积，正好是「除自己以外」的乘积。
#       顺带处理了元素为 0 的情况（乘法不受 0 的特殊影响），不需要额外判空。
# 复杂度：时间 O(n)，空间 O(1)（除输出数组外只用两个变量）


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1 for _ in range(size)]

        left = 1
        for i in range(size):
            res[i] *= left
            left *= nums[i]

        right = 1
        for i in range(size - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
