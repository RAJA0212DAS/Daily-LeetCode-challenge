class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right

        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cntDiv = [0] * (mx + 1)
        for d in range(1, mx + 1):
            s = 0
            for m in range(d, mx + 1, d):
                s += freq[m]
            cntDiv[d] = s

        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cntDiv[d]
            pairs = c * (c - 1) // 2
            m = d * 2
            while m <= mx:
                pairs -= exact[m]
                m += d
            exact[d] = pairs

        prefix = []
        gcds = []
        cur = 0
        for d in range(1, mx + 1):
            if exact[d]:
                cur += exact[d]
                prefix.append(cur)
                gcds.append(d)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(gcds[idx])

        return ans