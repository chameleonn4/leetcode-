# 509. Fibonacci Number / 斐波那契数
# 难度：简单    语言：Python3    日期：2026-10-20
# 链接：https://leetcode.cn/problems/fibonacci-number/
# 思路：直接按定义递归：F(0)=0，F(1)=1，F(n)=F(n-1)+F(n-2)。n ≤ 30 所以能过。
# 复杂度：时间 O(2^n)（指数级，同一项会被重复算很多次），空间 O(n)（递归栈）
# 进阶：改成迭代（两个变量滚动）就是 O(n) 时间、O(1) 空间；也可以加记忆化。


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (self.fib(n-1) + self.fib(n-2))
