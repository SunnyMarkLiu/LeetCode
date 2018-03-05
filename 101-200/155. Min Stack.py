#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-5 下午4:16
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        插入的时候就计算当前最小值，并随待插入的数据保留
        :type x: int
        :rtype: void
        """
        # 获取之前的最小值
        cur_min = self.getMin()
        if cur_min is None or cur_min > x:
            cur_min = x

        # 存储插入 x 和当前的最小值
        self.stack.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
