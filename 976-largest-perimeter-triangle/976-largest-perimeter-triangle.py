class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for i in range(1, len(nums)-1):
            if nums[n-i-2] + nums[n-i-1] > nums[n-i]:
                return nums[n-i-2] + nums[n-i-1] + nums[n-i]
            
        return 0