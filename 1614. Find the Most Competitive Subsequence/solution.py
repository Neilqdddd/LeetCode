class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        for idx, value in enumerate(nums):
            if not ans:
                ans.append(value)
            else:
                while ans and value < ans[-1] and (n + len(ans) - idx - 1) >= k:
                    ans.pop()
                if len(ans) < k:
                    ans.append(value)
        return ans


if __name__ == '__main__':
    nums = [84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61, 95,
            71]
    k = 24
    print(Solution().mostCompetitive(nums, k))
