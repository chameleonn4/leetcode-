# 234. Palindrome Linked List / 回文链表
# 难度：简单    语言：Python3    日期：2026-10-12
# 链接：https://leetcode.cn/problems/palindrome-linked-list/
# 思路：把链表的值依次读进数组，再和数组的反转比较（vals == vals[::-1]）。
#       链表没法随机访问，转成数组后判断回文就变成一句话。
# 复杂度：时间 O(n)，空间 O(n)
# 进阶：题目进阶要求 O(1) 空间——快慢指针找中点 + 反转后半段链表，再逐个比较。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]
