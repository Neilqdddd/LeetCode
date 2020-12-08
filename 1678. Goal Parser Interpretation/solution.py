class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = ''
        n = len(command)
        i = 0
        while i < n:
            if command[i] == 'G':
                ans += 'G'
                i += 1
            elif command[i] == '(' and command[i + 1] == ')':
                ans += 'o'
                i += 2
            elif command[i] == '(' and command[i + 1] == 'a':
                ans += 'al'
                i += 4
        return ans


if __name__ == '__main__':
    command = "G()()()()(al)"
    print(Solution().interpret(command))
