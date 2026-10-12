# 686. Repeated String Match / 重复叠加字符串匹配
# 难度：中等    语言：Python3    日期：2026-10-12
# 链接：https://leetcode.cn/problems/repeated-string-match/
# 思路：把 a 看成一条无限重复的磁带——第 i 个字符就是 a[i % n]，用 KMP 找 b 最早出现的位置 index。
#       因为 a∞ 的周期是 n，b 的最早起点一定落在第一个 a 里，所以循环条件是「起点 i-j < n」，
#       起点走到 n 还没匹配上说明永远匹配不上。
#       需要的份数 = (m + index - 1) // n + 1，也就是 b 从 index 起一直覆盖到第几份 a。
# 复杂度：时间 O(n + m)，空间 O(m)
# 图解：notes/0686-KMP回退原理图解.png、notes/0686-重复叠加字符串匹配图解.png
# 备注：generate_next 里的回退必须是 while（可能连续回退多次），这里曾经误写成 if，
#       会算出不符合定义的 next 数组（本题侥幸正确，换到别的 KMP 题就会错），已修正。


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def kmp(T:str , p:str):
            n = len(T)
            m = len(p)
            next = generate_next(p)
            i = 0
            j = 0
            while i-j < n :
                while T[i%n] != p[j] and j>0 :
                    j = next[j - 1]
                if T[i%n] == p[j]:
                    j += 1
                if j == m :
                    return i-j+1
                i += 1          #注意这个i+1的位置，并不是在if里，是在循环里
            return -1
        def generate_next(p:str):
            next = [0] * len(p)
            left = 0
            for right in range(1, len(p)):
                while left > 0 and p[left] != p[right]:   #必须用 while！回退一次后 p[left] 可能还对不上 p[right]，要连续回退；写成 if 算出的 next 不符合定义
                    left = next[left - 1]
                if p[left] == p[right]:
                    left += 1
                next[right] = left
            return next
        len_a = len(a)
        len_b = len(b)
        index = kmp(a,b)
        if index ==-1 :
            return -1
        if len_a - index > len_b :
            return 1
        return (len_b + index -1 ) // len_a + 1  #这个向上取整的写法值得学习
