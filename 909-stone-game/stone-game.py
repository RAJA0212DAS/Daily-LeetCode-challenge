class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo = {}

        def solve(i, j):
            if i == j:
                return piles[i]

            if (i, j) in memo:
                return memo[(i, j)]

            pickLeft = piles[i] - solve(i + 1, j)
            pickRight = piles[j] - solve(i, j - 1)

            memo[(i, j)] = max(pickLeft, pickRight)
            return memo[(i, j)]

        return solve(0, len(piles) - 1) > 0