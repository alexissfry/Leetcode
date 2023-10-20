class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(left,right,w):
            while left < right:
                temp = w[left]
                w[left] = w[right]
                w[right] = temp 
                left+=1
                right-=1

            return w 

        def reverseWord(w):
            n = len(w)
            start = end = 0

            while start < n:
                while end < n and w[end] != " ":
                    end += 1 
                reverse(start,end-1,w)
                start = end + 1 
                end += 1 
        
        reverse(0,len(s)-1,s)
        reverseWord(s)

        return s
        