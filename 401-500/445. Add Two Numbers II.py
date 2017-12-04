#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
reversing the lists is not allowed.

@author: MarkLiu
@time  : 17-12-4 上午11:05
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers_bug(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 将量表的数字从高位依次存入栈中
        stack_1 = []
        stack_2 = []
        while l1:
            v1 = l1.val
            l1 = l1.next
            stack_1.append(v1)

        while l2:
            v2 = l2.val
            l2 = l2.next
            stack_2.append(v2)

        # 从栈中依次从低位取出求和,并判断进位
        carry = 0
        head = n = ListNode(None)
        while len(stack_1) != 0 | len(stack_2) != 0 | carry != 0:
            v1 = 0 if len(stack_1) == 0 else stack_1.pop()
            v2 = 0 if len(stack_2) == 0 else stack_2.pop()

            s = v1 + v2 + carry
            carry = s // 10
            val = s % 10
            n.next = ListNode(val)
            n = n.next

        # 结果反转
        while head:
            tmp = head.next
            head.next = head
            head = tmp

        return head.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        a, b, c = 0, 0, 0
        while l1 is not None or l2 is not None:
            a = 0
            if l1 is not None:
                a = l1.val
                l1 = l1.next

            b = 0
            if l2 is not None:
                b = l2.val
                l2 = l2.next
            a = a + b + c
            c = a // 10
            a %= 10
            node = ListNode(a)
            node.next = res.next
            res.next = node

        if c != 0:
            node = ListNode(c)
            node.next = res.next
            res.next = node
        return res.next

    def reverse(self, l):
        pre = ListNode(-1)
        while l is not None:
            t = l.next
            l.next = pre.next
            pre.next = l
            l = t
        return pre.next


l1 = ListNode(1)
l1.next = ListNode(1)

l2 = ListNode(3)
l2.next = ListNode(2)

r = Solution().addTwoNumbers(l1, l2)
while r:
    print r.val
    r = r.next
