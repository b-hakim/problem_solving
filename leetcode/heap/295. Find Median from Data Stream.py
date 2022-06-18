import bisect
import heapq
import bisect


class MedianFinder1(object):

    def __init__(self):
        self.stream = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 1. BS the insert location
        # 2. Then insert

        ind = bisect.bisect_left(self.stream, num)
        self.stream.insert(ind, num)

    def findMedian(self):
        """
        :rtype: float
        """
        l = len(self.stream)
        # print(self.stream, l)

        if l % 2 == 0:
            return (self.stream[l // 2] + self.stream[l // 2 - 1]) / 2.0

        return self.stream[l // 2]


class MedianFinder(object):
    def __init__(self):
        self.small, self.higher = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1*num)

        if self.small and self.higher:
            if self.small[0]*-1 > self.higher[0]:
                v = heapq.heappop(self.small)
                heapq.heappush(self.higher, v*-1)

        if len(self.small) > len(self.higher) + 1:
            v = heapq.heappop(self.small)
            heapq.heappush(self.higher, -1 * v)

        if len(self.small)+ 1 < len(self.higher) :
            v = heapq.heappop(self.higher)
            heapq.heappush(self.small, -1 * v)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.higher):
            return (self.small[0]*-1 + self.higher[0])/2.0

        if len(self.small) > len(self.higher):
            return self.small[0]*-1

        return self.higher[0]


if __name__ == '__main__':
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    out = obj.findMedian()
    print(out)
    obj.addNum(3)
    out = obj.findMedian()
    print(out)