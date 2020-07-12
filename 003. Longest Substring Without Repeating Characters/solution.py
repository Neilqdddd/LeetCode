class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pool = {}

        maxlen = start = 0

        for index, value in enumerate(s):
            if value in pool:
                i = pool[value] + 1  # the place in s
                if i > start:  # change the starting position
                    start = i
            temp_len = index - start + 1  # the length
            if temp_len > maxlen:
                maxlen = temp_len
            pool[value] = index
        return maxlen


'''
Runtime: 40 ms, faster than 88.26% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 12.8 MB, less than 99.97% of Python online submissions for Longest Substring Without Repeating Characters.
'''
