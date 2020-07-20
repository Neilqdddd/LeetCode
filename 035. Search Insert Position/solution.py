'''
Brute force
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i + 1] > target:
                return i + 1
            i += 1


'''
Runtime: 28 ms, faster than 98.97% of Python online submissions for Search Insert Position.
Memory Usage: 13.3 MB, less than 21.24% of Python online submissions for Search Insert Position.
'''

''''
Binary Search
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return low


'''
Runtime: 36 ms, faster than 83.75% of Python online submissions for Search Insert Position.
Memory Usage: 13.1 MB, less than 74.51% of Python online submissions for Search Insert Position.
'''

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))
