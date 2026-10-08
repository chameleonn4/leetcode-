# 27. Remove Element / 移除元素
# 难度：简单    语言：Python3    日期：2026-10-08
# 链接：https://leetcode.cn/problems/remove-element/
# 思路：快慢指针原地删除。fast 从左到右扫描，遇到不等于 val 的元素就写到 slow 的位置，
#       再让 slow 后移一位；循环结束后 slow 正好等于保留下来的元素个数。
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
