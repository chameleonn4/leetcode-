# 455. Assign Cookies / 分发饼干
# 难度：简单    语言：Python3    日期：2026-10-20
# 链接：https://leetcode.cn/problems/assign-cookies/
# 思路：贪心 + 双指针。两个数组都先排序，然后用最小的饼干去试最小的胃口：
#       饼干够大就满足这个孩子（两个人指针都后移、答案 +1），不够大就把这块饼干浪费掉（只移饼干指针）。
#       因为小饼干喂不了大胃口，给"刚好能喂饱的最小的孩子"永远不亏。
# 复杂度：时间 O(n log n + m log m)，空间 O(1)（不计排序）

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index_g = 0
        index_s = 0
        res = 0
        while index_g < len(g) and index_s < len(s):
            if g[index_g] <= s[index_s]:
                res += 1
                index_g += 1
                index_s += 1
            else:
                index_s += 1
        return res
