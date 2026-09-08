class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums) # {2,20,4,10,3,5}
        res=0 #0
        for num in num_set: #num=20
            #find start point
            if num-1 not in num_set:#1
                current_start=num # 20
                current_streak=1# 1
                while current_start+1 in num_set:# 21
                    current_start+=1 #current_start = 
                    current_streak+=1 #  current_streak=
                res=max(current_streak,res) # res=4
        return res
                
        