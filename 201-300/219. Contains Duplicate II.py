#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 上午11:18
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map:
                if i - num_map[nums[i]] <= k:
                    return True
            num_map[nums[i]] = i

        return False
