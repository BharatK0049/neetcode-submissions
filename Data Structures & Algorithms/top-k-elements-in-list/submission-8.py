class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberFreq = {}

        for i in nums:
            if i in numberFreq:
                numberFreq[i] += 1
            else:
                numberFreq[i] = 1

        sorted_keys = sorted(numberFreq.keys(), key = lambda x: numberFreq[x], reverse=True)

        return sorted_keys[:k]
            