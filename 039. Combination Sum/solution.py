class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = [[] for i in range(target + 1)]

        for c in candidates:
            for i in range(1, target + 1):
                if c > i:
                    continue
                elif c == i:
                    ans[i].append([c])
                else:
                    for m in ans[i - c]:
                        ans[i].append(m + [c])
        return ans[target]


'''
Runtime: 32 ms, faster than 99.73% of Python online submissions for Combination Sum.
Memory Usage: 12.9 MB, less than 13.65% of Python online submissions for Combination Sum.
'''

if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))
