class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        sort = sorted(freq, key=freq.get)
        output = sort[-k:]
        
        
        return output