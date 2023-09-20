class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [False] * len(rooms)
        
        def checkRooms(index):
            #print(index, visited)
            nonlocal rooms

            if visited[index] == True:
                return 

            visited[index] = True 
            for key in rooms[index]:
                checkRooms(key)

        checkRooms(0)

        for v in visited:
            if v == False:
                return False
        return True
            

