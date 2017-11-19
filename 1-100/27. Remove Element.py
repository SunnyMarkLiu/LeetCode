#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
给定一个数组和一个值，将数组里所有等于这个值的元素全部移除。
不要分配额外空间给新的数组，空间复杂度为O(1). 数组元素的顺序可以改变。

@author: MarkLiu
@time  : 17-11-19 下午4:40
"""


class Solution(object):
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)

        for x in nums[:]:
            if x == val:
                nums.remove(x)

        return len(nums)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


nums_ = [3, 2, 2, 3]
val_ = 3
print Solution().removeElement(nums_, val_)
print nums_
