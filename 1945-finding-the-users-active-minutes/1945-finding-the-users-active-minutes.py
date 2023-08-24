'''
Goal: monitor usage statistics --> want to track number of unique active min a user has on Jira over a certain amount of time
How many diff unique minutes did this user perform an action on?
Given unique actions in form of array of arrays, each will store ID of user and what minute they performed it 
Also given an integer, from 1 to this integer how many different users performed actions exactly that number of unique minutes
 --> max number of unique minutes on which they performed an action  

 Output: store for every value from 1 up to given integer, how many users performed actions on that many unique minutes 
--> unique minute: specific user performed at least one action

 input1 = [["A", 1],["B", 2],["A", 3]], 2 --> {1: 1, 2: 1}
 input2 = [["A", 1],["A", 1],["B", 1],["A", 3]], 3 --> {1: 1, 2: 1, 3: 0}
 edgecase1 = [], 2 --> {1:0, 2:0}
 
n -> len(actions)
m -> numIds
k -> k
'''

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:    #key: user ID, values: unique minutes
        IDtoVal = {} # O(m)
        seen = set() # O(n)

        for a in logs:
            current = (a[0],a[1])
            if a[0] in IDtoVal:
                if current not in seen:
                    IDtoVal[a[0]] += 1
                    seen.add(current)
            else:
                IDtoVal[a[0]] = 1
                seen.add(current)
        
        result = [] # O(k)
        for i in range(1,k+1):
            result.append(0)

        for key,val in IDtoVal.items():
            result[val-1] += 1
            
        return result 

        
