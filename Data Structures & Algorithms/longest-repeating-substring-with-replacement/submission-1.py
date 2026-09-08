class Solution:
#"XYYX"
# l
#.   r
#count={x:2,y:2}
#maxfrquent=2
#maxlen=3
    def characterReplacement(self, s: str, k: int) -> int: 
        left=0
        right=0
        count={}
        maxfrequent=0
        maxlen=0
        while right < len(s):
            count[s[right]]=count.get(s[right],0)+1
            maxfrequent=max(count[s[right]],maxfrequent)
            while (right-left+1)-maxfrequent > k:
                count[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen