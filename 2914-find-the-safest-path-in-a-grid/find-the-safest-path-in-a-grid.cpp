#include <bits/stdc++.h>
using namespace std;

class Solution {
public:

    bool canReach(vector<vector<int>>& dist, int safe) {
        int n = dist.size();

        if (dist[0][0] < safe) return false;

        queue<pair<int,int>> q;
        vector<vector<bool>> vis(n, vector<bool>(n,false));

        q.push({0,0});
        vis[0][0] = true;

        int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!q.empty()) {
            auto [r,c] = q.front();
            q.pop();

            if (r == n-1 && c == n-1)
                return true;

            for (auto &d : dir) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr>=0 && nc>=0 && nr<n && nc<n &&
                    !vis[nr][nc] &&
                    dist[nr][nc] >= safe) {

                    vis[nr][nc] = true;
                    q.push({nr,nc});
                }
            }
        }
        return false;
    }

    int maximumSafenessFactor(vector<vector<int>>& grid) {

        int n = grid.size();

        vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
        queue<pair<int,int>> q;

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    dist[i][j]=0;
                    q.push({i,j});
                }
            }
        }

        int dir[4][2]={{1,0},{-1,0},{0,1},{0,-1}};

        while(!q.empty()){
            auto [r,c]=q.front();
            q.pop();

            for(auto &d:dir){
                int nr=r+d[0];
                int nc=c+d[1];

                if(nr>=0 && nc>=0 && nr<n && nc<n &&
                   dist[nr][nc]==INT_MAX){

                    dist[nr][nc]=dist[r][c]+1;
                    q.push({nr,nc});
                }
            }
        }

        int low=0, high=2*n, ans=0;

        while(low<=high){
            int mid=(low+high)/2;

            if(canReach(dist,mid)){
                ans=mid;
                low=mid+1;
            }
            else{
                high=mid-1;
            }
        }

        return ans;
    }
};