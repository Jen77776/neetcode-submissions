class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        char_set=set()
        length=0
        max_length=0
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                length=len(char_set)
                max_length=max(length,max_length)
                right+=1
            else:
                char_set.remove(s[left])
                left+=1
        return max_length
