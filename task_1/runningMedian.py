from typing import List


class RunningMedian:
    ints: List[int]

    def __init__(self, ints: List[int]=None):
        if not ints:
            self.ints=[]
        else:
            self.ints = ints
    
    def add(self, x: int):
        self.ints.append(x)
    
    def medina(self) -> float:
        self.ints.sort()
        if len(self.ints)%2!=0:
            return self.ints[(len(self.ints)-1)//2]
        else:
            return (self.ints[(len(self.ints)-1)//2]+self.ints[(len(self.ints)-1)//2+1])/2
    
# obj = RunningMedian([1,2,3])
# obj.add(0)
# print(obj.medina())

