class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        for i in range(n):
            j = n - 1 - i  # the postion of the number from right
            if digits[j] == 9:
                digits[j] = 0
            else:
                digits[j] += 1
                return digits
        return [1] + digits  # for the 999


if __name__ == '__main__':
    digits = [9, 9, 9]
    print(Solution().plusOne(digits))
