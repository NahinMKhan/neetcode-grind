class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        val = 1

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res[i] *= nums[j]
                 
        for i in range(len(nums) -1 , -1, -1):
            for j in range(i-1, -1, -1):
                res[i] *= nums[j]
        
        return res