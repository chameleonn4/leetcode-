# 1122. Relative Sort Array / 数组的相对排序
# 难度：简单    语言：Python3    日期：2026-10-16
# 链接：https://leetcode.cn/problems/relative-sort-array/
# 思路：计数排序。arr1 的值都不大（0 ~ 1000），于是开一个以「值本身」为下标的计数数组，
#       先统计 arr1 里每个数出现几次；再按 arr2 的顺序把对应的数整段放进答案并清零；
#       最后把计数数组里剩下的（即没在 arr2 出现过的）按下标从小到大补上——下标天然有序，
#       所以这一步直接就是升序，不用再排序。
# 复杂度：时间 O(n + max(arr1))，空间 O(max(arr1))


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        max_arr1 = max(arr1)
        nums_arr1 = [0] * (max_arr1 + 1)   # 下标就是值，初始全 0
        for x in arr1:
            nums_arr1[x] += 1              # 统计每个数出现次数

        nums = []
        for x in arr2:
            nums.extend([x] * nums_arr1[x])   # 按 arr2 顺序输出
            nums_arr1[x] = 0                  # 输出后清零

        for x in range(max_arr1 + 1):         # 剩下的元素按下标从小到大，天然就是升序
            nums.extend([x] * nums_arr1[x])

        return nums
