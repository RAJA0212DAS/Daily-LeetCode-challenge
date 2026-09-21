class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        int n = nums.size();

        if (k == 1) {
            return {1LL * n * (n + 1) / 2};
        }

        vector<long long> ans(k, 0);
        vector<long long> freq(k, 0);

        for (int x : nums) {
            int r = x % k;
            vector<long long> freq2(k, 0);

            ans[r]++;

            for (int j = 0; j < k; j++) {
                int prod = (j * r) % k;

                freq2[prod] += freq[j];
                ans[prod] += freq[j];
            }

            freq2[r]++;
            freq = freq2;
        }

        return ans;
    }
};