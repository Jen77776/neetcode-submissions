class Solution:
# [3,4,5,6,1,2]
#           l.   
#.          r
#.        m
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left +(right - left)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]