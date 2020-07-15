class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dif = float('inf')
        nums.sort()
        for i in range(len(nums)):
            p, q = i + 1, len(nums) - 1
            while p < q:
                sum = nums[i] + nums[p] + nums[q]
                if abs(target - sum) < abs(dif):
                    dif = target - sum
                if sum < target:
                    p += 1
                else:
                    q -= 1
            if dif == 0:
                break
        return target - dif


'''
Runtime: 92 ms, faster than 77.69% of Python online submissions for 3Sum Closest.
Memory Usage: 12.7 MB, less than 51.18% of Python online submissions for 3Sum Closest.
'''

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
