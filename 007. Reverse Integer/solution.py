class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1
        x *= sign
        '''
        也能使用list.reverse()
        '''
        ans = int(''.join(list(str(x))[::-1])) * sign
        return 0 if ans >= 2 ** 31 - 1 or ans <= -2 ** 31 else ans

'''
Runtime: 24 ms, faster than 53.69% of Python online submissions for Reverse Integer.
Memory Usage: 13 MB, less than 5.00% of Python online submissions for Reverse Integer
'''

if __name__ == '__main__':
    x = 1534236469
    print(Solution().reverse(x))
