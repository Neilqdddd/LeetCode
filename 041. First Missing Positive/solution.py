class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1

            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


'''
Runtime: 16 ms, faster than 98.35% of Python online submissions for First Missing Positive.
Memory Usage: 12.7 MB, less than 77.11% of Python online submissions for First Missing Positive.
'''

if __name__ == '__main__':
    nums = [7, 8, 9, 11, 12]
    print(Solution().firstMissingPositive(nums))
