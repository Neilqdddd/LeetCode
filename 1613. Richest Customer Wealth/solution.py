class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))
        return max_wealth


if __name__ == '__main__':
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(Solution().maximumWealth(accounts))
