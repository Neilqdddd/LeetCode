class Solution(object):
    def searchMatrix(self, matrix, target):
        # a binary search
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # matrix row*col
        row = len(matrix)
        if row == 0:
            return False

        col = len(matrix[0])

        left = 0
        right = row * col - 1  # the last element

        while left <= right:
            idx = (left + right) // 2
            element = matrix[idx // col][idx % col]
            if target == element:
                return True
            else:
                if target > element:
                    left = idx + 1
                else:
                    right = idx - 1
        return False


if __name__ == '__main__':
    matrix = []
    target = 0
    print(Solution().searchMatrix(matrix, target))
