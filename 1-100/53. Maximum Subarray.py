#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-5 上午11:03
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        暴力搜索: Time Limit Exceeded
        :type nums: List[int]
        :rtype: int
        """
        # 搜索 start end　下标
        n = len(nums)
        import sys
        ans = -sys.maxsize
        for start in range(0, n):
            for end in range(start + 1, n + 1):
                sum = 0
                for i in range(start, end):
                    sum += nums[i]

                if sum > ans:
                    ans = sum

        return ans
