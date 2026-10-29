class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                return nums[mid]
            #[3, 4, 5, 6, 1, 2]
            # l     m        r
            if nums[l] < nums[mid] and nums[mid] > nums[r]:
                l = mid + 1
            #[1, 2, 3, 4, 5, 6]
            # l     m        r
            if nums[l] < nums[mid] and nums[mid] < nums[r]:
                r = mid - 1
            
            minimum = min(minimum, mid)    
        return nums[minimum]


