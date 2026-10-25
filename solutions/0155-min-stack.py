# 155. Min Stack / 最小栈
# 难度：中等    语言：Python3    日期：2026-10-25
# 链接：https://leetcode.cn/problems/min-stack/
# 思路：辅助栈。用两个栈同步维护：stack 存原始元素，minstack 存「到当前位置为止的最小值」。
#       push 时若栈为空就都压入该值，否则 minstack 压入 min(val, minstack[-1])，于是 minstack 的栈顶恒为当前最小值；
#       pop 时两个栈同时弹出，最小值历史就自然「回退」了；top 取 stack 栈顶，getMin 取 minstack 栈顶。
#       进阶：也可以只用一个栈，额外存「入栈时的最小值」，或在每个节点旁挂一个 min 字段（面试常问的变体）。
# 复杂度：四个操作均摊 O(1)，空间 O(n)（两个栈各存一份）


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            self.stack.append(val)
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
