class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}

        for w in words:
            if w in freq.keys():
                freq[w] += 1
            else:
                freq[w] = 1

        keys = list(freq.keys())

        def sortingKey(k):
            return [-freq[k], k]

        keys.sort(key = sortingKey)
        return keys[:k]
        
        result = []
        for i in range(0,k):
            result.append(keys[i])

        return result