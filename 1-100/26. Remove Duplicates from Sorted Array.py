#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
注意使用的数组是有序数组!

除了基本的 in-place 算法外, 利用有序的特征, 双指针的方法
Since the array is already sorted, we can keep two pointers i and j,
where i is the slow-runner while j is the fast-runner.
As long as nums[i] = nums[j], we increment j to skip the duplicate.

@author: MarkLiu
@time  : 17-11-20 上午9:47
"""


class Solution(object):
    def removeDuplicates2(self, nums):
        """
        beat 40.58%
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums_dict = {}
        i = 0
        for j in range(len(nums)):
            if nums[j] not in nums_dict:
                nums[i] = nums[j]
                i += 1
            nums_dict[nums[j]] = True
        return i

    def removeDuplicates(self, nums):
        """
        beat 44.82%
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        # i 记录当前满足要求的最后一个数的下标
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


print(Solution().removeDuplicates([1, 1, 2]))
