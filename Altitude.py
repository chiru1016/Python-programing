class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0 # highest point
        low = 0 # lowest point
        for i in gain:
            low += i
            high = max(high,low) # take max of high and low
        return high