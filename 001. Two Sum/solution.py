class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pool={}
        for index, num in enumerate(nums):
            remain = target - num
            if remain not in pool:
                pool[num] = index
            else:
                return [pool[remain], index]

'''
Runtime: 24 ms, faster than 99.88% of Python online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 32.30% of Python online submissions for Two Sum.
'''
