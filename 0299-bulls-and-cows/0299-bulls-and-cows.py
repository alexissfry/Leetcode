class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        numBulls = 0 # number of bulls
        numCows = 0 # number of cows
        cSecret = Counter(secret) # count of every character in secret
        for i,digit in enumerate(guess): # go through guess
            if digit == secret[i]: # if it is in the same spot in secret
                numBulls += 1 # we found a bull
                if cSecret[digit] == 0: # if there are none of this digit left, replace one of our cows with this bull
                    numCows -= 1
                else:
                    cSecret[digit] -= 1 # remove this one from secret
            elif digit in cSecret and cSecret[digit] >= 1: # if this digit exists in cSecret
                numCows += 1 # we found a cow
                cSecret[digit] -= 1 # remove this one from secret
        return str(numBulls) + "A" + str(numCows) + "B" # format the string
        