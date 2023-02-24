from sortedcontainers import SortedList
class TweetCounts:

    def __init__(self):
        self.Time = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.Time[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ans = []
        
        while startTime <= endTime:
            l = bisect_left(self.Time[tweetName], startTime)
            if freq == "minute":startTime = min(startTime + 60, endTime + 1)
            if freq == "hour":startTime = min(startTime + 3600, endTime + 1)
            if freq == "day":startTime = min(startTime + 86400, endTime + 1)
            r = bisect_left(self.Time[tweetName], startTime)
            ans.append(r - l)
        
        return ans
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)