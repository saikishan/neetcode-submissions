class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        left, right = 0, len(heights) - 1

        while left < right:
            current = 0
            if heights[left] < heights[right]:
                current = heights[left] * (right - left)
                left += 1
            else:
                current = heights[right] * (right - left)
                right -= 1
            result = max(result, current)

        return result
