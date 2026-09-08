class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       length=len(nums)
       left_prefix=[1]*length
       right_prefix=[1]*length
       for i in range(1,length):
            left_prefix[i]=left_prefix[i-1]*nums[i-1]
       for i in range(length-2,-1,-1):
            right_prefix[i]=right_prefix[i+1]*nums[i+1]
       for i in range(length):
            left_prefix[i]*=right_prefix[i]
       return left_prefix
        
