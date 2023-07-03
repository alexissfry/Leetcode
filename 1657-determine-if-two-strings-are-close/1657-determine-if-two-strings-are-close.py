class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        
        for i in word1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for j in word2:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1
                        
        dict3 = dict()
        dict4 = dict()
        
        for i in dict1.values():
            if i in dict3:
                dict3[i] += 1
            else:
                dict3[i] = 1
        
        for j in dict2.values():
            if j in dict4:
                dict4[j] += 1
            else:
                dict4[j] = 1
                        
        return set(word1) == set(word2) and dict3 == dict4 
                
        