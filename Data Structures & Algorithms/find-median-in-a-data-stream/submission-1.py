class MedianFinder:

    def __init__(self):
        self.value = []


    def addNum(self, num: int) -> None:
        self.value.append(num)

    def findMedian(self) -> float:
        self.value.sort()
        return (self.value[len(self.value)//2] if (len(self.value)&1) else
        (self.value[len(self.value)//2] + self.value[len(self.value)//2-1])/2)
        