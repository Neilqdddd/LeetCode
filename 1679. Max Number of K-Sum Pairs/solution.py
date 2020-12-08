class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pool = {}
        count = 0
        for index, num in enumerate(nums):
            remain = k - num
            if remain not in pool:
                if num not in pool:
                    pool[num] = 1
                else:
                    pool[num] += 1
            else:
                count += 1
                pool[remain] -= 1
                if pool[remain] == 0:
                    del pool[remain]
        return count


if __name__ == '__main__':
    nums = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2]
    k = 3
    print(Solution().maxOperations(nums, k))
