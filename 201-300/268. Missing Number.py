#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
正常等差序列求和减去缺失的数组求和, 即可得到缺失的数据
@author: MarkLiu
@time  : 17-11-5 下午12:40
"""


class Solution(object):
    def missingNumber2(self, nums):
        """
        beat 44.82%
        :type nums: List[int]
        :rtype: int
        """
        tmp_nums = set(range(len(nums) + 1))
        return tmp_nums.difference(set(nums)).pop()

    def missingNumber(self, nums):
        """
        beat 84.49%
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n * (n + 1)) / 2 - sum(nums)


print Solution().missingNumber([0, 1, 3])
