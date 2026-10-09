# 28. Find the Index of the First Occurrence in a String / 找出字符串中第一个匹配项的下标
# 难度：简单    语言：Python3    日期：2026-10-10
# 链接：https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
# 思路：朴素匹配（双指针）。j 表示 needle 已匹配的长度，逐位比较 haystack[i] 与 needle[j]；
#       匹配就同时后移，失配则把起点右移一位（i = i - j + 1）并让 j 归零重新比。
#       j 走到 m 说明完全匹配，起始下标就是 i - j。
# 复杂度：时间 O(n·m)，空间 O(1)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0
        while j < m and i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        if j == m:
            return i - j
        else:
            return -1
