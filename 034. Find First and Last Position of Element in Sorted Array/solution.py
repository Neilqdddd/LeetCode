class Solution(object):
    def searchEngine(self, nums, target, left):
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (left and nums[mid] == target):
                high = mid
            else:
                low = mid + 1
        return low

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftpoint = self.searchEngine(nums, target, True)

        if leftpoint == len(nums) or nums[leftpoint] != target:
            return [-1, -1]
        return [leftpoint, self.searchEngine(nums, target, False) - 1]


'''
Runtime: 76 ms, faster than 56.69% of Python online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14 MB, less than 58.06% of Python online submissions for Find First and Last Position of Element in Sorted Array.
'''

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
