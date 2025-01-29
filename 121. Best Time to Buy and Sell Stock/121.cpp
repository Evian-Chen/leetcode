#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0], profit = 0;
        
        for (size_t i = 1; i < prices.size(); i++) {
            if (prices[i] < buy) {
                buy = prices[i];
            }
            profit = max(profit, prices[i]-buy);
        }

        return profit;
    }
};