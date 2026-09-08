class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        for str in strs:
            count=[0]*26
            for char in str:
                count[ord(char)-ord('a')]+=1
            anagram_map[tuple(count)].append(str)
        return list(anagram_map.values())