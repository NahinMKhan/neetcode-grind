class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        res = []

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        for i in range(k):
            maximum = 0
            maxKey = 0
            for key in frequencies:
                if frequencies[key] >= maximum:
                    maximum = frequencies[key]
                    maxKey = key
            res.append(maxKey)
            frequencies.pop(maxKey)
        
        return res