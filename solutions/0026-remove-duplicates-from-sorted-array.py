# 26. Remove Duplicates from Sorted Array / 删除有序数组中的重复项
# 难度：简单    语言：Python3    日期：2026-10-08
# 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
# 思路：快慢指针原地去重。数组有序，所以重复元素一定相邻；slow 指向已去重部分的末尾，
#       fast 向右扫描，发现 nums[fast] != nums[slow] 就先把 slow 右移一位再覆盖。
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
