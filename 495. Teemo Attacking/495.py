class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cur_time = 0
        total = 0
        for i in range(len(timeSeries)):
            if i == 0:
                cur_time = timeSeries[i]
            else:
                if timeSeries[i] > cur_time+duration-1:
                    total += duration
                elif timeSeries[i] <= cur_time+duration-1:
                    total += timeSeries[i]-cur_time
                cur_time = timeSeries[i]
        total += duration
        return total