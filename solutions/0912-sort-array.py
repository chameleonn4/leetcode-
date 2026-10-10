# 912. Sort an Array / 排序数组
# 难度：中等    语言：Python3    日期：2026-10-10
# 链接：https://leetcode.cn/problems/sort-array/
# 思路：随机选基准的三路快排。一次分区把数组切成【小于 ref | 等于 ref | 大于 ref】三段，
#       等于 ref 的那一段已经就位，只递归【小于段】和【大于段】。因为等值元素一次分区就全部
#       归位，所以题目故意加入大量重复元素时也不会退化（普通两路快排在全是重复元素时会 O(n²)）。
# 复杂度：期望时间 O(n log n)，最坏 O(n²)；递归栈期望 O(log n)
# 图解：notes/0912-三路快排分区图解.png（lt / i / gt 三个指针与每一步交换的全过程）


import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        '''
        这个题变态的地方在于普通快排根本AC不了，他会加入大量重复的元素来让你必须得三路快排，也就是原来
        是要分两个区，小于等于ref和大于等于ref，但是这个问题在于如果等于ref的值有很多，就会陷入循环
        于是解决办法就是三路快排，小于ref 等于ref 大于ref
        这里面比较难懂的是lt i gt 这三个变量代表什么
        lt代表等于ref的左边界
        i代表当前该处理的数组下标
        gt代表大于ref的左边界-1
        '''
        #三路快速排序，把数组分成三段：小于ref、等于ref、大于ref
        #随机选参考值ref，一次分区后，只递归【小于段】和【大于段】，等于段不用再排序
        def Randompartition(nums:list[int] , low:int ,high:int):
            i = random.randint(low,high)
            nums[i] , nums[low] = nums[low] , nums[i]
            # 三路分区，返回lt,gt两个边界
            return partition(nums , low , high)

        def partition(nums:list[int],low:int , high:int):
            ref = nums[low]
            lt = low    # lt左侧：全部 < ref；[low, lt-1] < ref
            gt = high   # gt右侧：全部 > ref；[gt+1, high] > ref
            i = low     # 当前遍历指针
            while i <= gt :
                if nums[i] < ref:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > ref:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else: # nums[i] == ref，直接跳过
                    i += 1
            # 返回小于区右边界、大于区左边界
            return lt, gt

        def quicksort(nums ,low , high):
            if low < high :
                # 三路分区拿到两段边界lt, gt
                lt, gt = Randompartition(nums , low , high)
                # 只递归 小于ref 和 大于ref 的区间，等于ref的[lt,gt]不用处理
                quicksort(nums , low , lt - 1)
                quicksort(nums , gt + 1 , high)

        quicksort(nums , 0 ,len(nums)-1)
        return nums
