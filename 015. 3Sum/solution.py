class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, ans)
        return ans

    def twoSum(self, nums, i, ans):
        p, q = i + 1, len(nums) - 1
        while p < q:
            sum = nums[i] + nums[p] + nums[q]
            if sum < 0 or (p > i + 1 and nums[p] == nums[p - 1]):
                p += 1
            elif sum > 0 or (q < len(nums) - 1 and nums[q] == nums[q + 1]):
                q -= 1
            else:
                ans.append([nums[i], nums[p], nums[q]])
                p += 1
                q -= 1


'''
Runtime: 828 ms, faster than 47.75% of Python online submissions for 3Sum.
Memory Usage: 16 MB, less than 58.50% of Python online submissions for 3Su
'''

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
