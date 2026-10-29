# 21. Merge Two Sorted Lists / 合并两个有序链表
# 难度：简单    语言：Python3    日期：2026-10-29
# 链接：https://leetcode.cn/problems/merge-two-sorted-lists/
# 思路：哑结点（dummy head）+ 尾指针。用 curr 指向已合并链表的尾部，每次比较
#       list1、list2 当前结点的值，把小的那个接到 curr.next，然后该链表前进一步，
#       curr 也前进一步。某个链表走空后，把另一个链表剩下的整段直接接上即可。
#       哑结点省掉了「先确定头结点」的特判；返回 dummy_head.next 才是真正的头。
#       注意比较用 <=，相等时优先取 list1，保证合并结果稳定。
# 复杂度：时间 O(m + n)，空间 O(1)（复用原结点，只改指针）


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)

        curr = dummy_head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy_head.next
