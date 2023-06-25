class Solution:
    def compress(self, chars: List[str]) -> int:
        run = 1
        result = []
        result.append(chars[0])
        
        if len(chars) == 1:
            return 1
        
        for c in range(1,len(chars)):
            if chars[c] == result[-1]:
                run += 1
            else:
                if run != 1:   
                    for ch in str(run):
                        result.append(ch)
                result.append(chars[c])
                run = 1
        if run != 1:   
            for ch in str(run):
                result.append(ch)
        
        print(result)
        
        for i in range(0,len(result)):
            chars[i] = result[i]
            
        return len(result)
            
        
        