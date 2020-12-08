class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = ''
        for i in range(1, n + 1):
            a += (bin(i))[2:]
        return int(a, 2) % (10 ** 9 + 7)


if __name__ == '__main__':
    n = 12
    print(Solution().concatenatedBinary(n))
