class Solution:
    def bestClosingTime(self, customers: str) -> int:
        currPen = 0
        hour = 0

        for s in customers:
            if s == "Y":
                currPen += 1 
        
        minPen = currPen

        for i in range(len(customers)):
            if customers[i] == "N":
                currPen += 1
            else:
                currPen -= 1

            if currPen < minPen:
                minPen = currPen
                hour = i+1


        return hour
            


