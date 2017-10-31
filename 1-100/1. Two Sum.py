#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-9-24 下午8:31
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return False

        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return buff_dict[nums[i]], i
            else:
                buff_dict[target - nums[i]] = i
