#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-4 下午9:49
"""


class Solution(object):
    def findPeakElement2(self, nums):
        """
        35 ms
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        for i in range(0, len(nums)):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

        return -1

    def findPeakElement(self, nums):
        """
        If num[i-1] < num[i] > num[i+1], then num[i] is peak
        If num[i-1] < num[i] < num[i+1], then num[i+1…n-1] must contains a peak
        If num[i-1] > num[i] > num[i+1], then num[0…i-1] must contains a peak
        If num[i-1] > num[i] < num[i+1], then both sides have peak
        """
        return self.findSubPeak(nums, 0, len(nums) - 1)

    def findSubPeak(self, nums, start, end):
        # 边界条件一：只剩下一个数
        if start == end:
            return start

        # 边界条件二：只剩下两个数
        if start + 1 == end:
            if nums[start] > nums[end]:
                return start
            return end

        mid = start + (end - start) // 2

        if nums[mid - 1] < nums[mid] > nums[mid + 1]:  # 找到峰值
            return mid
        elif nums[mid - 1] < nums[mid] < nums[mid + 1]:  # 峰值在右边
            return self.findSubPeak(nums, mid + 1, end)
        else:   # 峰值在左边以及峰值在左边和右边
            return self.findSubPeak(nums, start, mid - 1)
