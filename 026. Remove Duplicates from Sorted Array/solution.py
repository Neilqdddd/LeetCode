class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


'''
Runtime: 80 ms, faster than 51.64% of Python online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.6 MB, less than 18.59% of Python online submissions for Remove Duplicates from Sorted Array.
'''

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))
