class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        total = sum(stoneValue)
        dp = [0] * n
        pref = [0] * n
        sm = 0 
        for i in range(n-1,-1,-1):
            sm += stoneValue[i]
            pref[i] = sm
        for i in range(n-1,-1,-1):
            opt1 , opt2 , opt3 = stoneValue[i], stoneValue[i], stoneValue[i]
            if i + 1 < n:
                opt1 += pref[i+1] - dp[i+1]
                opt2 += stoneValue[i+1]
                opt3 += stoneValue[i+1]
            if i + 2 < n:
                opt2 += pref[i+2] - dp[i+2]
                opt3 += stoneValue[i+2]
            if i + 3 < n:
                opt3 += pref[i+3] - dp[i+3]
            dp[i] = max(opt1,opt2,opt3)
        if total-dp[0] == dp[0]:
            return "Tie"
        if 2 * dp[0] > total:
            return "Alice"
        return "Bob"
