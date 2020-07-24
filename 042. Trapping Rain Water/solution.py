'''
Two point 算法
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        pool = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    pool += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    pool += (right_max - height[right])
                right -= 1
        return pool


'''
Runtime: 32 ms, faster than 95.20% of Python online submissions for Trapping Rain Water.
Memory Usage: 13.1 MB, less than 89.53% of Python online submissions for Trapping Rain Water.
'''

'''
DP 
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        n = len(height)
        left_dp = [0 for i in range(n)]
        right_dp = [0 for i in range(n)]

        left_dp[0], right_dp[-1] = height[0], height[-1]

        for i in range(1, n):
            left_dp[i] = max(left_dp[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            right_dp[i] = max(right_dp[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(left_dp[i], right_dp[i]) - height[i]
        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
