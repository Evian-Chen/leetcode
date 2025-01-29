#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for (size_t i = 0; i < prices.size() - 1; i++) {
            if (prices[i+1]-prices[i] > 0) {
                profit += (prices[i+1]-prices[i]);
            }
        }

        return profit;
    }
};