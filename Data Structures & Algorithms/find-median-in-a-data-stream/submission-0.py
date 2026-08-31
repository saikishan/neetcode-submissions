import heapq

class MedianFinder:

    def __init__(self):
        self.lHeap = []
        self.rHeap = []

    def lInsert(self, value):
        heapq.heappush(self.lHeap, -1 * value)

    def lTop(self):
        if len(self.lHeap) == 0:
            return None
        return -1 * self.lHeap[0]

    def lPop(self):
        return -1 * heapq.heappop(self.lHeap)

    def rInsert(self, value):
        heapq.heappush(self.rHeap, value)

    def rTop(self):
        if len(self.rHeap) == 0:
            return None
        return self.rHeap[0]

    def rPop(self):
        return heapq.heappop(self.rHeap)



    def balance(self):

        diff = len(self.lHeap) - len(self.rHeap)

        if diff == 2:
            self.rInsert(self.lPop())

        elif diff == -2:
            self.lInsert(self.rPop())





    def insert(self, value):
        if len(self.lHeap) == 0 or self.lTop() >= value:
            self.lInsert( value )
        else:
            self.rInsert( value )


    def addNum(self, num: int) -> None:
        self.insert(num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.lHeap) > len(self.rHeap):
            return (self.lTop()) / 1.0
        elif len(self.lHeap) < len(self.rHeap):
            return (self.rTop()) / 1.0
        return (self.rTop() + self.lTop()) / 2.0
        
        