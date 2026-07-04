class Solution {
public:
    int ans = INT_MAX;

    void dfs(int node, vector<int>& vis,
             vector<vector<pair<int,int>>>& adj) {

        vis[node] = 1;

        for (auto &it : adj[node]) {
            int nxt = it.first;
            int wt = it.second;

            ans = min(ans, wt);

            if (!vis[nxt]) {
                dfs(nxt, vis, adj);
            }
        }
    }

    int minScore(int n, vector<vector<int>>& roads) {

        vector<vector<pair<int,int>>> adj(n + 1);

        for (auto &e : roads) {
            int u = e[0];
            int v = e[1];
            int w = e[2];

            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }

        vector<int> vis(n + 1, 0);

        dfs(1, vis, adj);

        return ans;
    }
};