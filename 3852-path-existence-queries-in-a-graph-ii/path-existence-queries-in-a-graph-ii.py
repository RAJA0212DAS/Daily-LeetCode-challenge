import bisect

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        order = sorted(range(n), key=lambda x: nums[x])
        sorted_vals = [nums[node] for node in order]
        rank = [0] * n
        for pos, node in enumerate(order):
            rank[node] = pos

        LOG = 17
        jump = [[0] * n for _ in range(LOG)]
        for p in range(n):
            jump[0][p] = bisect.bisect_right(sorted_vals, sorted_vals[p] + maxDiff) - 1

        for k in range(1, LOG):
            for p in range(n):
                jump[k][p] = jump[k-1][jump[k-1][p]]

        def min_steps(pu, pv):
            if pu == pv: return 0
            pos = pu
            steps = 0
            for k in range(LOG - 1, -1, -1):
                if jump[k][pos] < pv:       
                    pos = jump[k][pos]
                    steps += (1 << k)
            if jump[0][pos] >= pv:          
                return steps + 1
            return -1                       

        answer = []
        for u, v in queries:
            pu, pv = rank[u], rank[v]
            if pu > pv: pu, pv = pv, pu    
            answer.append(min_steps(pu, pv))
        return answer