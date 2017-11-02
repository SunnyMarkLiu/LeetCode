#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
只有一个数出现一次, 其他数都出现两次, 所有由两次出发采用按位异或运算符 ^
关键点:
    0^0=0,0^1=1   0异或任何数＝任何数
    0^0=0,1^1=0   任何数异或任何数＝0 (出现两次)

@author: MarkLiu
@time  : 17-11-2 下午12:58
"""
import collections


class Solution(object):
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_counter = collections.Counter(nums)
        for key in num_counter.iterkeys():
            if num_counter[key] == 1:
                return key
        return None

    def singleNumber3(self, nums):
        """
        beats 45.12%
        :type nums: List[int]
        :rtype: int
        """
        num_counter = {}
        for num in nums:
            num_counter[num] = num_counter.get(num, 0) + 1

        num_counter = {v: k for k, v in num_counter.iteritems()}
        if 1 in num_counter:
            return num_counter[1]
        return None

    def singleNumber(self, nums):
        """
        Trick: 按位异或运算符^
        参与运算的两个值，如果两个相应位相同，则结果为0，否则为1。即：0^0=0， 1^0=1， 0^1=1， 1^1=0
        例如：10100001^00010001=10110000
        0^0=0,0^1=1     0异或任何数＝任何数
        1^0=1,1^1=0     1异或任何数－任何数取反

        beats 90.85%
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res


print Solution().singleNumber([3, 2, 2])
