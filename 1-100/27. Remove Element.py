#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
给定一个数组和一个值，将数组里所有等于这个值的元素全部移除。
不要分配额外空间给新的数组，空间复杂度为O(1). 数组元素的顺序可以改变。

@author: MarkLiu
@time  : 17-11-19 下午4:40
"""


class Solution(object):
    def removeElement1(self, nums, val):
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

    def removeElement2(self, nums, val):
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

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)

        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:  # 如果找到等于 val 的数，用最后一个数替换 val，减少 nums 的长度，同时丢弃最后一个数，n--
                nums[i] = nums[n - 1]
                n -= 1  # reduce array size by one
            else:
                i += 1
        return n


nums_ = [3, 2, 2, 3]
val_ = 3
print(Solution().removeElement(nums_, val_))
print(nums_)
