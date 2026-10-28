# 136. Single Number / 只出现一次的数字
# 难度：简单    语言：Python3    日期：2026-10-28
# 链接：https://leetcode.cn/problems/single-number/
# 思路：异或。异或的性质：a ^ a = 0，a ^ 0 = a，且满足交换律和结合律。
#       出现两次的数两两异或后全部抵消，剩下的就是那个只出现一次的数。
#       题目保证有且只有一个数出现一次，其余都出现两次，所以整体异或即可。
# 复杂度：时间 O(n)，空间 O(1)


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
