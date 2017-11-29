#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-11-29 下午9:15
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        for i, num in enumerate(nums):
            if target <= num:
                return i

        return len(nums)

print Solution().searchInsert([0.1, 2, 3], 1)
