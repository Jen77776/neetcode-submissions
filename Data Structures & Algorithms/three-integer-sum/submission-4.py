class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #
        length=len(nums) #len=6
        i=0
        res=[]
        for i in range(len(nums)-2): #i=0
            j=i+1 #j=1
            k=length-1 #k=5
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                if nums[j]+nums[k]== -nums[i]:
                    res.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1] :
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif nums[j]+nums[k]< -nums[i]:
                    j+=1
                else:
                    k-=1
        return res
            



        