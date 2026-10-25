# 189. Rotate Array / 轮转数组
# 难度：中等    语言：Python3    日期：2026-10-25
# 链接：https://leetcode.cn/problems/rotate-array/
# 思路：三次反转，不用额外数组。整个数组反转 + 前 k 个反转 + 后 n-k 个反转，
#       就等价于整体右移 k 位（因为「右移 k」= 「左移 n-k」，而三段反转正好对应一次切分）。
#       k 要先对 n 取模，否则 k >= n 时会越界。
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
    def reverse(self, nums, i , j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
