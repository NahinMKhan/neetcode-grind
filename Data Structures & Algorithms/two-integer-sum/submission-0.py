class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [min(hash[diff], i), max(hash[diff], i)]
            else:
                hash[n] = i
        