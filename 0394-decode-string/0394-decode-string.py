class Solution:
    def decodeString(self, s: str) -> str:
        if not s: # if no string return nothing
            return ""
        i = 0 # pointer to go through string
        start = "" # characters at the start of the string
        while s[i].isalpha(): # while it is a character
            start += s[i] # add this to the start
            i += 1 # move forward
            if i == len(s): # if we reached the end of the string then it's all characters
                return start # just return it
        k = "" # k -- the number of times to repeat the next segment
        while s[i].isdigit(): # while looking at a number
            k += s[i] # add it to the end of k
            i += 1 # move forward 
        j = i+1 # we must have hit a "[", so skip past it
        num = 1 # number of open "["
        while num: # while there is a "[" open
            j += 1 # move forward
            num = num + (s[j] == "[") - (s[j] == "]") # add to num if we find a "[", subtract if we find a "]"
        return start + int(k) * self.decodeString(s[i+1:j]) + self.decodeString(s[j+1:]) 
        # our resultant string has to start with "start"
        # since "i" keeps track of the starting "[" and "j" keeps track of the closing "]", we want to multiply the encoded_string, self.decodeString(s[i+1:j]), by "k"
        # then we decode the rest of the string, s[j+1:], in case there is anything left
        