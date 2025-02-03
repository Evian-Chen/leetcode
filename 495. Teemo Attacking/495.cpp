#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int curTime = 0, total = 0;
        for (size_t i=0; i<timeSeries.size(); i++) {
            if (i == 0) {
                curTime = timeSeries[i];
            }
            else {
                if (timeSeries[i] > curTime+duration-1) {
                    total += duration;
                }
                else {
                    total += (timeSeries[i]-curTime);
                }
                curTime = timeSeries[i];
            }
        }
        total += duration;
        return total;
    }
};