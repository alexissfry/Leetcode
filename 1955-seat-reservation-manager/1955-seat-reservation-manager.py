from heapq import heapify, heappop, heappush
# heapify(list) --> turn list into a heap in-place (akin to list.sort())
# heappop(heap) --> heap pop from the list and return the smallest value
# heappupsh(heap, val) --> heap push val onto the list

class SeatManager:

    def __init__(self, n: int):
        self.seatHeap = list(range(1,n+1))
        heapify(self.seatHeap)

    def reserve(self) -> int:
        seatNum = heappop(self.seatHeap)
        return seatNum

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seatHeap,seatNumber)
        
        

'''
Edgecase behavior:
- If seats are all reserved and another user tries to reserve, return -1

["SeatManager", "reserve", "reserve", "unreserve", "reserve"]
[[5], [], [], [2], []]

seats = {1:False, 2:False, 3:False, 4:False, 5:False}

seats = {1:True, 2:False, 3:False, 4:False, 5:False}

seats= {1:True, 2:True, 3:False, 4:False, 5:False}

seats= {1:True, 2:False, 3:False, 4:False, 5:False}

seats= {1:True, 2:True, 3:False, 4:False, 5:False}

'''

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)