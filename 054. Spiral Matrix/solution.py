class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        row, col = len(matrix), len(matrix[0])
        M = row * col
        ans = []
        count = 0
        i = 0
        j = 0
        while count != M:
            '''
            bad simulation but it works
            '''
            for right in range(i, col):
                count += 1
                ans.append(matrix[i][right])
            if count == M:
                return ans
            for down in range(j + 1, row):
                count += 1
                ans.append(matrix[down][-(j + 1)])
            if count == M:
                return ans
            for left in range(i + 2, col + 1):
                count += 1
                ans.append(matrix[row - 1][-left])
            if count == M:
                return ans
            for up in range(j + 2, row):
                count += 1
                ans.append(matrix[-up][j])

            if count == M:
                return ans
            i += 1
            j += 1
            row -= 1
            col -= 1

        print(count)
        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(Solution().spiralOrder(matrix))
