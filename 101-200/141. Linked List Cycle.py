#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-1 下午3:03
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        用快慢指针判断单链表环，找到环入口,扩展到判断两个链表是否相交
        (http://www.nowamagic.net/librarys/veda/detail/1842)

        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        # 偶数                    奇数
        while fast is not None and fast.next is not None:  # 快指针到达最后的 null,　或最后节点的下一个节点是 null,　取决于链表长度的奇偶
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
