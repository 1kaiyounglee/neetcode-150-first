class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        match = defaultdict(list)
        for word in strs:
            key_list = [0] * 26
            for c in sorted(word):
                key_list[ord(c) - ord('a')] += 1
            
            print(tuple(key_list))
            match[tuple(key_list)].append(word)



        return list(match.values())