# 169. Majority Element / 多数元素
# 难度：简单    语言：Python3    日期：2026-10-28
# 链接：https://leetcode.cn/problems/majority-element/
# 思路：哈希表计数。用 dict 统计每个数出现的次数，统计的同时就检查是否超过总数的一半，
#       超过就直接返回它——题目保证多数元素一定存在，所以中途一定能命中，不用遍历完。
#       （进阶可以用 Boyer-Moore 摩尔投票法，空间 O(1) 且只需一趟：相同数计数 +1，
#         不同就抵消，票数非零时的数就是答案。）
# 复杂度：时间 O(n)，空间 O(n)（哈希表）


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else :
                hashmap[num] = 1
            if hashmap[num] > (len(nums))/2:
                return num
