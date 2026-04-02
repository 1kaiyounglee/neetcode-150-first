class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        
        for char in t:
            if char not in freq:
                return False
            elif freq[char] - 1 == 0:
                del freq[char]
            else:
                freq[char] -= 1
        
        return len(freq) == 0 