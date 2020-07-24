class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)

        def backtrack(first=0):
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return ans


'''
Runtime: 24 ms, faster than 91.27% of Python online submissions for Permutations.
Memory Usage: 12.8 MB, less than 44.99% of Python online submissions for Permutations.
'''

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))
