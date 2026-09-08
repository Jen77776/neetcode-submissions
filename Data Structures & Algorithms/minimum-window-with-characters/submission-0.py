class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        for char in t:
            need[char]=need.get(char,0)+1
        l=0
        r=0
        window = {}
        valid=0
        min_len = float('inf')
        start=0
        for r in range(len(s)):
            char = s[r]
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid+=1
            while valid == len(need):
                if r - l + 1 < min_len:
                    start = l 
                    min_len = r - l +1
                left_char = s[l]
                l += 1

                if left_char in need:
                    if need[left_char] == window[left_char]:
                        valid -= 1
                    window[left_char] -= 1
        return "" if min_len == float('inf') else s[start : start + min_len]