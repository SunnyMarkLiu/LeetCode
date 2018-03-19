#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 上午9:46
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getListLen(self, heada, headb):
        # 获取两个链表的长度
        lena = 0
        lenb = 0
        while heada:
            lena += 1
            heada = heada.next

        while headb:
            lenb += 1
            headb = headb.next

        return lena, lenb

    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        lena, lenb = self.getListLen(headA, headB)

        # 让较长的链表先走差值步
        while lena < lenb:
            headB = headB.next
            lena += 1

        while lenb < lena:
            headA = headA.next
            lenb += 1

        # 此时 A B 等长，同时走，每次比较
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    # 方法二，利用环，A走到链表尾部后走B的头，B走到尾部走A的头，两者必然相遇，因为所走的路程相等最多为两个链表长度之和
    #         如果A=B=None，则走到链表尾部也没找到相等的结点，说明没有交叉；A=B!=None 返回交点
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        mov_a, mov_b = headA, headB

        while mov_a != mov_b:
            mov_a = mov_a.next if mov_a else headB
            mov_b = mov_b.next if mov_b else headA

        return mov_a
