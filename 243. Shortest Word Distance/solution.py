class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = float('inf')
        pos = [None, None]
        for index, value in enumerate(words):
            if value not in [word1, word2]:
                continue
            pos[value == word2] = index
            if None in pos:
                continue
            ans = min(ans, abs(pos[0] - pos[1]))
        return ans





if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(Solution().shortestDistance(words, word1, word2))
