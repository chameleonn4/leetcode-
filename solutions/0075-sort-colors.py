# 75. Sort Colors / 颜色分类
# 难度：中等    语言：Python3    日期：2026-10-28
# 链接：https://leetcode.cn/problems/sort-colors/
# 思路：荷兰国旗问题，三指针一趟原地排序。
#       left 指向当前 0 段（红色）的右边界，right 指向当前 2 段（蓝色）的左边界，index 是扫描位置：
#       - nums[index] == 0：和 nums[left] 交换，0 就位了，left += 1、index += 1；
#       - nums[index] == 2：和 nums[right] 交换，2 就位了，right -= 1，但**index 不动**——
#         因为从右边换过来的值还没检查过，必须重新判断它是什么颜色；
#       - nums[index] == 1（白色）：已经在中间，index += 1。
# 复杂度：时间 O(n)，空间 O(1)


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1
