#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-4 下午5:33
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        找到数组中 target 的下标范围，注意二分判断的边界条件

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = self.findFirst(nums, target)
        right_index = self.findLast(nums, target, left_index)
        return [left_index, right_index]

    def findFirst(self, nums, target):
        left_index = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:  # 注意二分判断的边界条件，因为要找到最左边的下标，如果 mid 的值比 target 大，继续 right = mid - 1
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                left_index = mid

        return left_index

    def findLast(self, nums, target, left_index):
        last_index = -1
        if left_index == -1:
            return -1

        left, right = left_index, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:  # 注意二分判断的边界条件，因为要找到最右边的下标，如果 mid 的值比 target 大，继续 left = mid + 1
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                last_index = mid

        return last_index
