class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1

        for num, count in freq.items():
            buckets[count].append(num)
        print(buckets)
        
        sol = []

        for i in range(len(buckets) - 1 , 0, -1):
            for num in buckets[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol