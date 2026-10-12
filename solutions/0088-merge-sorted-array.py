# 88. Merge Sorted Array / 合并两个有序数组
# 难度：简单    语言：Python3    日期：2026-10-12
# 链接：https://leetcode.cn/problems/merge-sorted-array/
# 思路：双指针 + 临时数组。i 指 nums1 的有效部分、j 指 nums2，每次把较小的那个追加进 temp；
#       某个数组走完后，把另一个剩余的整段补上；最后把 temp 拷回 nums1 的前 m+n 个位置。
# 复杂度：时间 O(m+n)，空间 O(m+n)
# 进阶：题目要求不返回新数组、原地合并时可以「从后往前」双指针，空间降到 O(1)——
#       因为 nums1 的后 n 个格子本来就是空的，从最大的开始往 nums1 尾部填就不会覆盖还没比较的元素。


class Solution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0

        temp = []
        # 两个数组都没走完时，取较小值
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        # 把剩余元素补上
        while i < m:
            temp.append(nums1[i])
            i += 1
        while j < n:
            temp.append(nums2[j])
            j += 1
        # 拷贝回 nums1
        for idx in range(len(temp)):
            nums1[idx] = temp[idx]
