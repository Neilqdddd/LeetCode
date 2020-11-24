class Solution(object):
    # Fibonacci Number
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_num = 1
        second_num = 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(n - 2):
                third = first_num + second_num
                first_num = second_num
                second_num = third
            return second_num


class Solution(object):
    # dynamic programming
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            dp = [1] * (n + 1)
            dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]


if __name__ == '__main__':
    n = 6
    print(Solution().climbStairs(n))
