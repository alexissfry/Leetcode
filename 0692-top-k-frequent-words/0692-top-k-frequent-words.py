class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
	    return [word for (word,count) in sorted(Counter(words).most_common(), key = lambda x:(-x[1],x[0]))[:k]] 
        