class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        inProv = set()
        numProvs = 0
        
        def province(city):
            if city in inProv:
                return 

            inProv.add(city)

            for j in range(len(isConnected)):
                if isConnected[city][j] == 1:
                    province(j)

        for i in range(len(isConnected)):
            if i in inProv:
                continue 
            province(i)
            numProvs += 1
        
        return numProvs