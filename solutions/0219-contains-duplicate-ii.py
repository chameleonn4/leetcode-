# 219. Contains Duplicate II / 存在重复元素 II
# 难度：简单    语言：Python3    日期：2026-10-20
# 链接：https://leetcode.cn/problems/contains-duplicate-ii/
# 思路：哈希表维护「最近 k 个元素」这个滑动窗口。遍历到 nums[i] 时：
#       先查它是否已经在窗口里——在就说明存在 j < i 且 i - j <= k，直接 True；
#       然后把它放进窗口，如果窗口元素个数超过 k，就把 nums[i-k] 移出去（保证窗口里只有前 k 个元素）。
# 复杂度：时间 O(n)，空间 O(min(n, k))

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            nums_dict[nums[i]] = 1
            if len(nums_dict) > k:
                del nums_dict[nums[i - k]]
        return False
