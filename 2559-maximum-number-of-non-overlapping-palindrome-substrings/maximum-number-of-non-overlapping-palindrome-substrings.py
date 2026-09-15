'''
class Solution(object):
    def palindrome(self, s, i, j):
        return s[i:j+1] == s[i:j+1][::-1]
    def solve(self, s, k, i, j, dp):
        if i >= len(s) or j >= len(s):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if self.palindrome(s, i, j):
            take = 1 + self.solve(s, k, j + 1, j + k, dp)
            grow = self.solve(s, k, i, j + 1, dp)
            slide = self.solve(s, k, i + 1, j + 1, dp)
            dp[i][j] = max(take, grow, slide)
            return dp[i][j]
        grow = self.solve(s, k, i, j + 1, dp)
        slide = self.solve(s, k, i + 1, j + 1, dp)
        dp[i][j] = max(grow, slide)
        return dp[i][j]
    def maxPalindromes(self, s, k):
        n = len(s)
        if k == 1:
            return n
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return self.solve(s, k, 0, k - 1, dp)
'''
class Solution(object):
    def isPal(self, s, n):
        isPalindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            isPalindrome[i][i] = True 
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1   #l = i + j - 1
                if s[i] == s[j]:
                    if l == 2:
                        isPalindrome[i][j] = True 
                    else:
                        isPalindrome[i][j] = isPalindrome[i + 1][j - 1]
        return isPalindrome
    def maxPalindromes(self, s, k):
        n = len(s)
        isPalindrome = self.isPal(s, n)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if isPalindrome[i][j]:
                    if j + k < n:
                        take = 1 + dp[j + 1][j + k]
                    else:
                        take = 1
                    grow = dp[i][j + 1]
                    slide = dp[i + 1][j + 1]
                    dp[i][j] = max(take, grow, slide)
                else:
                    grow = dp[i][j + 1]
                    slide = dp[i + 1][j + 1]
                    dp[i][j] = max(grow, slide)
        return dp[0][k - 1]