#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-1 上午11:21
"""


class Solution(object):
    def search(self, nums, target):
        """
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
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < nums[high]:  # 右半段为有序的
                if nums[mid] < target <= nums[high]:  # target 在有序的右半段
                    low = mid + 1
                else:  # 左边
                    high = mid - 1
            elif nums[mid] > nums[high]:  # 左半段为有序的
                if nums[low] <= target < nums[mid]:  # target 在有序的左半段
                    high = mid - 1
                else:  # 右边
                    low = mid + 1
            else:  # 如果 mid 和 high 相等，则 high　减一
                high -= 1

        return False
