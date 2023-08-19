class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        availChange = {5:0, 10:0, 20:0}

        for i in bills:
            if i == 5:
                availChange[5] += 1
            elif i == 10:
                if availChange[5] > 0:
                    availChange[5] -= 1
                    availChange[10] += 1
                else:
                    return False
            elif i == 20:
                if availChange[5] > 0 and availChange[10] > 0:
                    availChange[5] -= 1
                    availChange[10] -= 1
                elif availChange[5] >= 3:
                    availChange[5] -= 3
                else:
                    return False
    
            print(availChange)
        return True 
            
