#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-1 下午1:14
"""


# _*_ coding: utf-8 _*_

class Solution(object):
    def findDuplicate(self, nums):
        """
        注意　n+1　个数，大小为　1－n
        假设数组中没有重复，那我们可以做到这么一点，就是将数组的下标和1到n每一个数一对一的映射起来。
        比如数组是213,则映射关系为0->2, 1->1, 2->3。假设这个一对一映射关系是一个函数f(n)，其中n是下标，
        f(n)是映射到的数。如果我们从下标为0出发，根据这个函数计算出一个值，以这个值为新的下标，
        再用这个函数计算，以此类推，直到下标超界。实际上可以产生一个类似链表一样的序列。
        比如在这个例子中有两个下标的序列，0->2->3。但如果有重复的话，这中间就会产生多对一的映射，
        比如数组2131,则映射关系为0->2, {1，3}->1, 2->3。这样，我们推演的序列就一定会有环路了，
        这里下标的序列是0->2->3->1->1->1->1->…，而环的起点就是重复的数。

        快慢指针：http://www.nowamagic.net/librarys/veda/detail/1842

        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:  # 找到相遇的位置
                break

        # 从开始位置(0)和第一次相遇点(fast)同时以步长１
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                break

        return slow
