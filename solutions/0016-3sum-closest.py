# 16. 3Sum Closest / 最接近的三数之和
# 难度：中等    语言：Python3    日期：2026-10-08
# 链接：https://leetcode.cn/problems/3sum-closest/
# 思路：排序 + 双指针。固定 nums[i]，剩下两数用左右指针向中间逼近 target；
#       和等于 target 就直接返回（不可能更近），否则随时更新最接近的答案；
#       外层跳过重复的 i，内层移动指针时也跳过重复元素以减少无谓计算。
# 复杂度：时间 O(n²)，空间 O(1)（不含排序）


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]  # 初始化为第一个三元组的和

        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    k -= 1
                    # 跳过重复
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    # 跳过重复
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return best
