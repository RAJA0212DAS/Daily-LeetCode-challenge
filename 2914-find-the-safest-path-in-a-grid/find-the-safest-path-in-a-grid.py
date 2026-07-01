from collections import deque

class Solution(object):

    def canReach(self, dist, safe):
        n = len(dist)

        if dist[0][0] < safe:
            return False

        q = deque([(0, 0)])
        visited = set()
        visited.add((0, 0))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            if r == n-1 and c == n-1:
                return True

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if (0 <= nr < n and
                    0 <= nc < n and
                    (nr, nc) not in visited and
                    dist[nr][nc] >= safe):

                    visited.add((nr, nc))
                    q.append((nr, nc))

        return False


    def maximumSafenessFactor(self, grid):
        n = len(grid)

        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if (0 <= nr < n and
                    0 <= nc < n and
                    dist[nr][nc] == float('inf')):

                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        low, high = 0, 2*n
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.canReach(dist, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans