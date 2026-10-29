# 141. Linked List Cycle / 环形链表
# 难度：简单    语言：Python3    日期：2026-10-29
# 链接：https://leetcode.cn/problems/linked-list-cycle/
# 思路：哈希表记录走过的结点。从头遍历，每到一个结点先查它是否访问过：
#       已经出现过说明又绕回来了，必然有环，直接返回 True；没出现过就加入集合，
#       然后继续 next。走到 None 说明链表有尽头，没有环，返回 False。
#       注意存的是结点对象本身（靠 id 判断），不是 val——val 重复不代表同一个结点。
# 复杂度：时间 O(n)，空间 O(n)
# 进阶：题目进阶要求 O(1) 空间——快慢指针（Floyd 判圈），有环必相遇、无环快指针先到 None。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodeset = set()

        while head:
            if head in nodeset:
                return True
            nodeset.add(head)
            head = head.next
        return False
