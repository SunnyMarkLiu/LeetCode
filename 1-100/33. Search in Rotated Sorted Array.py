#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-2-28 下午8:21
"""


class Solution:
    def search2(self, nums, target):
        """
        有序数组进行了旋转操作，找到其中的某个值，先采用二分法找到最小值，即找到 pivot 的位置
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        start = 0
        stop = len(nums) - 1

        min_index = 0
        # 先找到最小值以及对应的下标
        while start < stop - 1:
            if nums[start] == target:
                return start
            if nums[stop] == target:
                return stop

            if nums[start] < nums[stop]:
                min_index = start
                break

            mid = (start + stop) // 2

            if nums[mid] == target:
                return mid

            if nums[start] < nums[mid]:
                start = mid
            elif nums[start] > nums[mid]:
                stop = mid

        if stop - start == 1:
            if nums[start] < nums[stop]:
                min_index = start
            else:
                min_index = stop

        if nums[min_index] == target:
            return min_index

        # 根据最小值确定二分法检索 target
        if min_index == 0:
            start = 0
            stop = len(nums) - 1
        elif target < nums[0]:  # 右边
            start = min_index
            stop = len(nums) - 1
        elif target > nums[0]:  # 左边
            start = 0
            stop = min_index

        while start < stop:
            if nums[start] == target:
                return start
            if nums[stop] == target:
                return stop

            mid = (start + stop) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                stop = mid
            elif target > nums[mid]:
                start = mid

            if stop - start == 1:
                return -1

        return -1

    def search(self, nums, target):
        """
        https://www.cnblogs.com/grandyang/p/4325648.html
        0　　1　　2　　 *4　　5　　6　　7*
        7　　0　　1　　 *2　　4　　5　　6*
        6　　7　　0　　 *1　　2　　4　　5*
        5　　6　　7　　 *0　　1　　2　　4*
        *4　　5　　6　　 7* 　0　　1　　2
        *2　　4　　5　　 6*　　7　　0　　1
        *1　　2　　4　　 5*　　6　　7　　0

        二分搜索法的关键在于获得了中间数后，判断下面要搜索左半段还是右半段，我们观察上面红色的数字都是升序的，
        由此我们可以观察出规律，如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，
        则左半段是有序的，*我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内*，
        这样就可以确定保留哪半边了

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[high]: # 右半段为有序的
                # 在有序的右半段用首尾两个数组来判断目标值是否在这一区域内
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:   # 不在有序的右半段
                    high = mid - 1
            else:   # 左半段为有序的
                # 在有序的右半段用首尾两个数组来判断目标值是否在这一区域内
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:   # 不在有序的左半段
                    low = mid + 1

        return -1


print(Solution().search([4, 5, 6, 7, 8, 0, 1, 2, 3], 4))
print(Solution().search([0, 1, 2, 3, 4, 5, 6, 7, 8], 3))
print(Solution().search([1, 3], 3))
