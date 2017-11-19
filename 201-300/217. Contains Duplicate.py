#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
给定一个整数数组，判断其中是否包含重复元素。

方法一: 先将数组进行排序（排序的复杂度），排序后比较每个元素与后一个元素是否相等即可。
方法二: 将出现的数字存入 HashMap 中, 判断数字是否出现的 HashMap 中。
方法三: 没有重复的数组相当于集合，利用Python的set，将数组转换成集合，若长度与原来相等则说明没有重复。

@author: MarkLiu
@time  : 17-11-19 下午5:38
"""


class Solution(object):
    def containsDuplicate2(self, nums):
        """
        beat 89.64%
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        return len(set(nums)) < len(nums)

    def containsDuplicate2(self, nums):
        """
        beat 74.66%
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def containsDuplicate(self, nums):
        """
        beat 19.60%
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True
            nums_dict[num] = True
        return False
