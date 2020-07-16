''''
在3 sum的基础上确定剩下的， 思想基本一样先确定一个点然后两个边界相互移动
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                self.threeSum(nums, i, target, ans)
        return ans

    def threeSum(self, nums, i, target, ans):
        for j in range(i + 1, len(nums)):
            if j == i + 1 or nums[j - 1] != nums[j]:
                self.twoSum(nums, i, j, target, ans)

    def twoSum(self, nums, i, j, target, ans):
        p, q = j + 1, len(nums) - 1
        while p < q:
            sum = nums[i] + nums[j] + nums[p] + nums[q]
            if sum < target or (p > j + 1 and nums[p] == nums[p - 1]):
                p += 1
            elif sum > target or (q < len(nums) - 1 and nums[q] == nums[q + 1]):
                q -= 1
            else:
                ans.append([nums[i], nums[j], nums[p], nums[q]])
                p += 1
                q -= 1


'''
Runtime: 1156 ms, faster than 15.19% of Python online submissions for 4Sum.
Memory Usage: 12.7 MB, less than 92.93% of Python online submissions for 4Sum.
'''

if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    target = 0
    print(Solution().fourSum(nums, target))
