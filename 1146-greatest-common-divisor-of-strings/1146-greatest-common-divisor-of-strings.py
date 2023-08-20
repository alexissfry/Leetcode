class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        len1 = len(str1)
        len2 = len(str2)

        minLen = min(len1,len2)
        startChar = str1[0]
        prefix = ""

        for i in range(0,minLen):
            if str1[i] == str2[i]:
                prefix += str1[i]
            else:
                break

        lenPre = len(prefix)

        if lenPre == 0:
            return ""

        def valid(i):
            # checks if the prefix[0:i] is what you want to return
            if len1%i == 0 and len2%i == 0:
                iter1 = len1//i
                iter2 = len2//i

                for n in range(iter1):
                    if prefix[0:i] != str1[n*i:i*(n+1)]:
                        return False 
                for m in range(iter2):
                    if prefix[0:i] != str2[m*i:i*(m+1)]:
                        return False 
                return True
            return False
                
        while lenPre > 0:
            if valid(lenPre):
                return prefix[0:lenPre]
            lenPre -= 1
            
        return ""
