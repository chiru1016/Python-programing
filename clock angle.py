class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mini = 6 * minutes
        hour = 0 if hour is 12 else hour
        hr = (30 * hour) + (0.5 * minutes)
        result = 0
        if mini > hr:
            result = mini - hr
        else:
            result = hr - mini
        return min(result, 360 - result)

