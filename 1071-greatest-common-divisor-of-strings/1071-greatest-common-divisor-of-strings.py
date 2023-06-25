class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        minLen = min(len(str1), len(str2))
        result = ""
        
        for i in range(minLen):
            if str1[i] == str2[i]:
                result += str1[i]
            else:
                break
        
        def div(poop):
            
            if len(poop) == 0:
                return True
            
            if (len(str1)%len(poop) == 0) and (len(str2)%len(poop) == 0):
                div1 = len(str1)//len(poop)
                div2 = len(str2)//len(poop)
                for i in range(div1):
                    j = i*len(poop)
                    if str1[j:j+len(poop)] != poop:
                        return False
                for i in range(div2):
                    j = i*len(poop)
                    if str2[j:j+len(poop)] != poop:
                        return False
                return True
            return False
        
        while True:
            if div(result):
                return result
            else:
                result = result[:-1]
            
        return result