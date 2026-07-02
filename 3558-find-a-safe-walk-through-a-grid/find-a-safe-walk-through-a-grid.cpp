
using namespace std;

class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {

        int m = grid.size();
        int n = grid[0].size();

        int startHealth = health - grid[0][0];

        if (startHealth <= 0)
            return false;

        queue<pair<int,int>> q;

        vector<vector<int>> best(m, vector<int>(n, -1));

        best[0][0] = startHealth;
        q.push({0,0});

        int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!q.empty()) {

            auto [r,c] = q.front();
            q.pop();

            if (r == m-1 && c == n-1)
                return true;

            for (auto &d : dir) {

                int nr = r + d[0];
                int nc = c + d[1];

                if (nr>=0 && nc>=0 && nr<m && nc<n) {

                    int newHealth = best[r][c] - grid[nr][nc];

                    if (newHealth > 0 && newHealth > best[nr][nc]) {

                        best[nr][nc] = newHealth;
                        q.push({nr,nc});
                    }
                }
            }
        }

        return false;
    }
};