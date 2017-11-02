#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-9-24 下午9:08
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 1:
            return False

        buff_dict = {}
        for i in range(len(numbers)):
            if numbers[i] in buff_dict:
                if buff_dict[numbers[i]] < i:
                    return buff_dict[numbers[i]] + 1, i + 1
                return i + 1, buff_dict[numbers[i]] + 1

            buff_dict[target - numbers[i]] = i
