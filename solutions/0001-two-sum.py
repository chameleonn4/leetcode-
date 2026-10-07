# 1. Two Sum / 两数之和
# 难度：简单    语言：Python3    日期：2026-10-07
# 链接：https://leetcode.cn/problems/two-sum/
# 思路：哈希表。遍历数组时，先查 target - num 是否出现过，再把自己存进哈希表。
# 复杂度：时间 O(n)，空间 O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i


if __name__ == "__main__":
    # 本地自测
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    print("All tests passed.")
