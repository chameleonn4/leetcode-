# 349. Intersection of Two Arrays / 两个数组的交集
# 难度：简单    语言：Python3    日期：2026-10-16
# 链接：https://leetcode.cn/problems/intersection-of-two-arrays/
# 思路：排序 + 双指针。两个数组都排好序后，用 left_1 / left_2 同步推进：
#       相等就是交集元素，谁小谁往后走。因为已排序，去重只要「和上一个加入的元素比一比」即可，
#       不需要额外用 set。
# 复杂度：时间 O(n log n + m log m)，空间 O(1)（不计返回的列表）

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  # 对 nums1 进行排序
        nums2.sort()  # 对 nums2 进行排序

        left_1 = 0  # 指向 nums1 的指针
        left_2 = 0  # 指向 nums2 的指针
        res = []

        # 优化：由于数组已排序，结果去重只需判断上一个加入的元素即可
        while left_1 < len(nums1) and left_2 < len(nums2):
            if nums1[left_1] == nums2[left_2]:
                # 只有 res 为空或当前元素与上一个加入的元素不同才加入结果，避免重复
                if not res or nums1[left_1] != res[-1]:
                    res.append(nums1[left_1])
                left_1 += 1
                left_2 += 1
            elif nums1[left_1] < nums2[left_2]:
                left_1 += 1
            else:  # nums1[left_1] > nums2[left_2]
                left_2 += 1
        return res
