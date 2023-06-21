class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set()
        vowels.update(["a","e","i","o","u","A","E","I","O","U"])
        s_list = list(s)
        
        left = 0
        right = len(s)-1
        
        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            elif s_list[left] in vowels:
                right -= 1
            elif s_list[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        
        swapped_string = ''.join(s_list)  # Convert the list back to a string
        return swapped_string
        
        
        