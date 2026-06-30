#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfSubstrings(string s) {

        int n = s.size();
        int left = 0;
        int ans = 0;

        unordered_map<char, int> count;

        for (int right = 0; right < n; right++) {

            count[s[right]]++;

            while (count['a'] > 0 &&
                   count['b'] > 0 &&
                   count['c'] > 0) {

                ans += (n - right);

                count[s[left]]--;
                left++;
            }
        }

        return ans;
    }
};