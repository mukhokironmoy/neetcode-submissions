class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict({})

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        counts = list(freq.items())

        counts.sort(key= lambda item:item[1], reverse=True)

        topk = []
        for i in range(k):
            topk.append(counts[i][0])

        return topk