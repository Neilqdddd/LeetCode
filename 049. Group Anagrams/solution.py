import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for i in strs:
            ans[tuple(sorted(i))].append(i)
        return ans.values()


'''
Runtime: 84 ms, faster than 89.61% of Python online submissions for Group Anagrams.
Memory Usage: 17.1 MB, less than 37.43% of Python online submissions for Group Anagrams.
'''

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
