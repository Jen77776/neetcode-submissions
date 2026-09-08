class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        count={}# count={x:2,y:2}
        res=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            mostFrequency=max(count.values()) #2
            elementBeenReplaced=(right-left+1)-mostFrequency #2
            if elementBeenReplaced <= k:
                res=max(res,right-left+1) #res=4
                right+=1
            else:
                count[s[left]]-=1
                left+=1
        return res
#"XYYX"
# l
#     r

#stringLength-mostFrequency=elementBeenReplacyed