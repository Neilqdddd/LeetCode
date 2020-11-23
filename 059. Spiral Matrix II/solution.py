class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[False for i in range(n)] for i in range(n)]
        start_col = 0  # start col position
        end_col = n  # end col position
        start_row = 0  # start row position
        end_row = n  # end row position
        count = 1
        while start_col < end_col and start_row < end_row:

            for i in range(start_col, end_col):
                # first layer from left to the right
                # after finish the start_row add 1
                ans[start_row][i] = count
                count += 1
            start_row += 1

            for i in range(start_row, end_row):
                ans[i][end_col - 1] = count
                count += 1
            end_col -= 1

            for i in range(end_col - 1, start_col - 1, -1):
                ans[end_row - 1][i] = count
                count += 1
            end_row -= 1

            for i in range(end_row - 1, start_row - 1, -1):
                ans[i][start_col] = count
                count += 1
            start_col += 1
        return ans


if __name__ == '__main__':
    n = 4
    print(Solution().generateMatrix(n))
