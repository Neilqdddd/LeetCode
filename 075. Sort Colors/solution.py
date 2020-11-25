class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start, current, end = 0, 0, len(nums) - 1
        while current <= end:
            if nums[current] == 0:
                nums[start], nums[current] = nums[current], nums[start]
                current += 1
                start += 1
            elif nums[current] == 2:
                nums[end], nums[current] = nums[current], nums[end]
                end -= 1
            else:
                current += 1
        return nums


if __name__ == '__main__':
    nums = [1, 2, 0]
    print(Solution().sortColors(nums))
