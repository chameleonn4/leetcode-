# 56. Merge Intervals / 合并区间
# 难度：中等    语言：Python3    日期：2026-10-25
# 链接：https://leetcode.cn/problems/merge-intervals/
# 思路：排序 + 一次遍历。按左端点升序排序后，从左往右扫：
#       如果结果里最后一个区间的右端点 < 当前区间的左端点，说明两者不重叠，直接把新区间加进去；
#       否则两者重叠，把最后一个区间的右端点更新成两者的较大值（合并）。
# 复杂度：时间 O(n log n)，空间 O(n)（不含返回结果）

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        这个排序intervals.sort(key = lambda x: x[0])依靠的是
        key这个排序依据参数 x 是intervals里的的interval
        '''
        intervals.sort(key=lambda x: x[0])

        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
