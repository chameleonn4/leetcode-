# 763. Partition Labels / 划分字母区间
# 难度：中等    语言：Python3    日期：2026-10-28
# 链接：https://leetcode.cn/problems/partition-labels/
# 思路：贪心。先用哈希表记录每个字母最后出现的位置 letter_map。
#       然后从左往右扫，用 end 维护「当前这一段必须延伸到的最右位置」：
#       遇到 s[i] 就 end = max(end, letter_map[s[i]])（这一段里出现的字母，
#       它的最后一次出现也必须包含在本段内，否则那个字母就会跨段出现）；
#       当 i == end 时，说明本段可以切一刀了，段长是 end - start + 1，然后 start = i + 1。
# 复杂度：时间 O(n)，空间 O(字符集大小)

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_map = dict()
        for i in range(len(s)):
            letter_map[s[i]] = i
        res = []
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, letter_map[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
