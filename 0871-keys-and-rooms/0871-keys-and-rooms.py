class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        This only works if we visit the rooms sequentially
        currKeys = set(rooms[0])

        for i in range(len(rooms)):
            print(i,currKeys)
            if i == 0:
                continue 

            elif i not in currKeys:
                return False

            for key in rooms[i]:
                currKeys.add(key)
            i += 1 

        return True
        '''
        visited = [False for i in range(len(rooms))]
        visited[0] = True 

        def dfs(rooms, index):
            nonlocal visited 

            for key in rooms[index]:
                #print(rooms, key, visited)
                if visited[key] == False:
                    visited[key] = True 
                    dfs(rooms, key)
            return 

        dfs(rooms, 0)

        for visit in visited:
            if not visit:
                return False 
        return True 
        