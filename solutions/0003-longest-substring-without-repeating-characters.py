# 3. Longest Substring Without Repeating Characters / 无重复字符的最长子串
# 难度：中等    语言：Python3    日期：2026-10-16
# 链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 思路：滑动窗口 + 哈希表。右指针先把字符收进窗口并计数；一旦当前字符出现次数 > 1，
#       就不断右移左指针把字符移出窗口，直到窗口内没有重复；此时窗口长度就是一个合法答案。
#       left / right 都只单调右移，所以每个字符最多进出窗口各一次。
# 复杂度：时间 O(n)，空间 O(字符集大小)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # 滑动窗口左边界
        right = 0 # 滑动窗口右边界
        window = dict() # 记录窗口内每个字符出现的次数
        ans = 0 # 记录最长无重复子串的长度

        while right < len(s):
            # 将当前字符加入窗口，统计出现次数
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            # 如果当前字符出现次数大于1，说明有重复，需要收缩左边界
            while window[s[right]] > 1:
                window[s[left]] -= 1 # 左边界字符出现次数减少
                left += 1 # 左边界右移，缩小窗口

            # 更新最长无重复子串的长度
            ans = max(ans, right - left + 1)
            right += 1 # 右边界右移，扩大窗口

        return ans # 返回结果
