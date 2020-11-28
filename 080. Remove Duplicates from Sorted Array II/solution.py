class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        count = 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1

            i += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    print(Solution().removeDuplicates(nums))
