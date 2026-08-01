class Solution:
    def predictTheWinner(self, nums):
        total = sum(nums)

        def getPlayer1Max(player1, start, end, turn):
            if start > end:
                return player1

            if turn:
                left = getPlayer1Max(player1 + nums[start], start + 1, end, False)
                right = getPlayer1Max(player1 + nums[end], start, end - 1, False)
                return max(left, right)
            else:
                left = getPlayer1Max(player1, start + 1, end, True)
                right = getPlayer1Max(player1, start, end - 1, True)
                return min(left, right)

        playerOneMax = getPlayer1Max(0, 0, len(nums) - 1, True)

        if total % 2:
            return playerOneMax >= (total + 1) // 2
        return playerOneMax >= total // 2