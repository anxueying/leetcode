# encoding: utf-8

"""
@author: Shelly An
@contact: 81247054@qq.com
@software: PyCharm
@file: 两数之和.py
@time: 2019/1/23 18:06
"""

import datetime

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


# test
t = Solution()
begin = datetime.datetime.now()
print(t.twoSum([2, 7, 11, 15], 9))
end = datetime.datetime.now()
print('运行时间：', end-begin)