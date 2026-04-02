class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        
        match = defaultdict(list)
        for word in strs:
            key_list = [0] * 26
            print(sorted(word))
            for c in sorted(word):
                key_list[ord(c) - ord('a')] += 1
            print(key_list)
            
            match[tuple(key_list)].append(word)



        return list(match.values())