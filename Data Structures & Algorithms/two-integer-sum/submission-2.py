class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        match = {}

        for num in nums:
            if num not in match.keys():
                diff = target - num
                if diff in match.keys():
                    return [match[diff], count]
                match[num] = count
            else:
                if num * 2 == target:
                    return [match[num], count]
            
            count += 1