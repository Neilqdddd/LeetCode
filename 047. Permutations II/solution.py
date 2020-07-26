class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)

        def backtrack(first=0):
            if first == n and nums[:] not in ans:
                ans.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return ans


'''
Runtime: 1148 ms, faster than 9.99% of Python online submissions for Permutations II.
Memory Usage: 12.9 MB, less than 65.33% of Python online submissions for Permutations II.
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        def bk(A, i, j, res):
            if i == j - 1:
                res.append(A[:])
                return
            for k in range(i, j):
                if k == i or A[i] != A[k]:
                    A[k], A[i] = A[i], A[k]
                    bk(A[:], i + 1, j, res)

        bk(nums, 0, len(nums), ans)
        return ans


'''
Runtime: 84 ms, faster than 47.03% of Python3 online submissions for Permutations II.
Memory Usage: 13.9 MB, less than 80.30% of Python3 online submissions for Permutations II.
'''

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
