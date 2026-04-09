class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        arrays = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hash[num] = 1 + hash.get(num, 0)

        for n, c in hash.items():
            arrays[c].append(n)

        result = []
        for i in range(len(arrays) - 1, 0, -1):
            for j in arrays[i]:
                result.append(j)
                if(len(result)) == k:
                    return result







        