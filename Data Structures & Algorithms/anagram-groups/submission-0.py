class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for string in strs:
            char = [0] * 26
            for c in string:
                char[ord(c) - ord('a')] += 1
            hash[tuple(char)].append(string)
    
        return list(hash.values())
