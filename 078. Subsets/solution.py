class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for num in nums:
            print(output)
            output += [cur + [num] for cur in output]

        return output


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
