# 20. Valid Parentheses / 有效的括号
# 难度：简单    语言：Python3    日期：2026-10-12
# 链接：https://leetcode.cn/problems/valid-parentheses/
# 思路：栈。左括号一律入栈；遇到右括号就看栈顶是不是同类型的左括号——是就弹出，
#       不是（或者栈已经空了）直接返回 False。遍历完栈还非空说明有左括号没闭合。
#       另外长度为奇数时不可能配对，可以先一步判掉。
# 复杂度：时间 O(n)，空间 O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        result = False
        stack = list()
        n = len(s)
        if n%2 ==0 :
            for ch in s:
                if ch == '(' or ch == '{' or ch == '[':
                    stack.append(ch)
                elif ch == ')':
                    if stack and stack[-1] == '(':#python里面是可以用-1来写栈顶的
                        stack.pop()
                    else:
                        return False
                elif ch == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif ch == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            if len(stack) == 0:
                result = True
        return result
