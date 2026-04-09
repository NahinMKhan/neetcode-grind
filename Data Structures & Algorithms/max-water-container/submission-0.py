class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        
        for i in range(0, len(heights)-1):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                area = height * width
                maxA = max(maxA, area)
                j += 1
            i += 1
        return maxA
            
                