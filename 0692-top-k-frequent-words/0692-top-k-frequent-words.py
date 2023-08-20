class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)

        pairs = []

        for i in counter:
            pairs.append((-counter[i],i))
        print(pairs)

        heapq.heapify(pairs)

        return [heapq.heappop(pairs)[1] for _ in range(k)]