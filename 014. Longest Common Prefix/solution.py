class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)


'''
Runtime: 20 ms, faster than 84.40% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.1 MB, less than 5.09% of Python online submissions for Longest Common Prefix.
'''

if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
