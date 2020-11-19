class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = self.nextSequence(n, ['1', 'D'])
        return ''.join(str)

    def nextSequence(self, n, prevSeq):
        '''
        1 1
        2 1 11
        3 11 21
        4 21 1211
        5 1211 111221
        6 111221 312211
        sliding window
        '''
        if n == 1:
            return prevSeq[:-1]

        nextSeq = []
        preDigit = prevSeq[0]

        count = 1

        for digit in prevSeq[1:]:
            if digit == preDigit:
                count += 1
            else:
                nextSeq.extend([str(count), preDigit])
                preDigit = digit
                count = 1
        nextSeq.append('D')

        return self.nextSequence(n - 1, nextSeq)


if __name__ == '__main__':
    n = 5
    print(Solution().countAndSay(n))
