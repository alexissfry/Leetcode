class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        if len(digits) == 0:
            return []

        combos = []
        for letter in nums[digits[0]]:
            combos.append(letter)

        i = 1
        while i < len(digits):
            new_combos = []

            for combo in combos:
                for letter in nums[digits[i]]:
                    new_combos.append(combo+letter)

            combos = new_combos
            i += 1

        return combos
