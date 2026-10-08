# 2. Add Two Numbers / 两数相加
# 难度：中等    语言：Python3    日期：2026-10-08
# 链接：https://leetcode.cn/problems/add-two-numbers/
# 思路：哑结点 + 逐位相加。两个链表本来就低位在前，所以直接从头部同步遍历，
#       carry 记录进位，任一链表走完就补 0，最后进位不为 0 再补一个结点。
# 复杂度：时间 O(max(m, n))，空间 O(1)（不含返回的链表）


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()  # 哑节点，方便处理链表头
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
