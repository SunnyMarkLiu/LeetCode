#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-18 下午10:33
"""


class Solution:
    def majorityElement1(self, nums):
        """
        方法一：Hash table
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            if num_count[num] > len(nums) / 2:
                return num

    def majorityElement(self, nums):
        """
        方法二：对数组进行排序，那么出现次数超过一半的元素必定是数组中的中间元素，返回这个元素即可。
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]