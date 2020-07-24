class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def dfs(curr, nums):
            if sum(curr) > target:
                return
            if sum(curr) == target:
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(curr + [nums[i]], nums[i + 1:])

        dfs([], candidates)
        return ans


'''
Runtime: 104 ms, faster than 40.16% of Python online submissions for Combination Sum II.
Memory Usage: 13 MB, less than 11.56% of Python online submissions for Combination Sum II.
'''

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
