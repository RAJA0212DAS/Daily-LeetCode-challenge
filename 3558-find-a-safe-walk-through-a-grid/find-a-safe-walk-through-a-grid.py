from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):

        m, n = len(grid), len(grid[0])

        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = start_health

        q = deque([(0, 0)])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:

            r, c = q.popleft()

            if r == m-1 and c == n-1:
                return True

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    new_health = best[r][c] - grid[nr][nc]

                    if new_health > 0 and new_health > best[nr][nc]:

                        best[nr][nc] = new_health
                        q.append((nr, nc))

        return False