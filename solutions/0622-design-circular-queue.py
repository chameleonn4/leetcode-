# 622. Design Circular Queue / 设计循环队列
# 难度：中等    语言：Python3    日期：2026-10-12
# 链接：https://leetcode.cn/problems/design-circular-queue/
# 思路：数组多开一格（size = k + 1），front / rear 每次移动都对 size 取模，
#       用「牺牲一个格子」的方式区分空和满：
#         rear == front            → 空
#         (rear + 1) % size == front → 满
#       这样就不需要额外的计数器或标志位，入队写 queu[rear] 再 rear 后移，出队只把 front 后移。
# 复杂度：所有操作 O(1)，空间 O(k)


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k + 1
        self.queu = [None for _ in range(self.size)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queu[self.rear] = value
        self.rear = (1+self.rear)%self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queu[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queu[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1)%self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
