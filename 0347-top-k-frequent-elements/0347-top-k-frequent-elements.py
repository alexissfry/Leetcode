class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        result = []
        
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        i = 0
        for f in freq.keys():
            if i == k:
                break
            else:
                result.append(f)
                i += 1
        
        return result