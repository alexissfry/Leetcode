class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ran = {}
        mag = {}
        
        for i in ransomNote:
            if i in ran:
                ran[i] += 1
            else:
                ran[i] = 1
                
        for j in magazine:
            if j in mag:
                mag[j] += 1
            else:
                mag[j] = 1
        
        for n in ran:
            if mag.get(n):
                if ran[n] > mag[n]:
                    return False
            else:
                return False 
            
        return True