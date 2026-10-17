class Solution:
    def binarySearch(self, l: int, r: int, array: List[int], target: int) -> int:
        if l > r:
            return -1

        m = (l + r) // 2 

        if array[m] == target:
            return m

        if array[m] > target:
            return self.binarySearch(l, m - 1, array, target)
        
        if array[m] < target:
            return self.binarySearch(m + 1, r, array, target)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in matrix:
            x = self.binarySearch(0, len(i) - 1, i, target)
            if x != -1:
                return True
        return False
        