# 394. Decode String / 字符串解码
# 难度：中等    语言：Python3    日期：2026-10-27
# 链接：https://leetcode.cn/problems/decode-string/
# 思路：双栈。用 res 保存「当前这一层括号」已经解出来的字符串，num 保存正在读到的重复次数：
#       遇到数字：num = num * 10 + int(ch)（位数可能多位，所以要乘 10 累加）；
#       遇到 '['：说明进入一层新的括号，把外层的 res 和重复次数 num 分别压进 stack1 / stack2，
#                 然后把 res 清空、num 清零，从新的一层重新开始拼；
#       遇到 ']'：这一层结束，弹出外层的 res（stack1）和重复次数（stack2），
#                 把本层解出的 res 重复 cur_num 次，再拼回外层：res = cur_res + res * cur_num；
#       遇到字母：直接 res += ch。
# 复杂度：时间 O(输出串长度 L)（每个字符至少被拼接一次），空间 O(L + 嵌套深度)


class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)   # 字符串数字转数组
            elif ch == '[':
                stack1.append(res)
                stack2.append(num)
                res = ""
                num = 0
            elif ch == ']':
                cur_res = stack1.pop()
                cur_num = stack2.pop()
                res = cur_res + res * cur_num
            else:
                res += ch
        return res
