#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-11-3 下午7:42
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_counter = {}
        for num in nums:
            num_counter[num] = num_counter.get(num, 0) + 1
        result = []
        for k in num_counter.keys():
            if num_counter[k] == 1:
                result.append(k)

        return result

print Solution().singleNumber([1, 2, 1, 3, 2, 5])
