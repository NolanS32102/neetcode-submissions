class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            currWater = (right - left) * min(heights[right], heights[left])
            maxWater = max(maxWater, currWater)
            if heights[right] <= heights[left]:
                right -= 1
            else:
                left += 1
        

        return maxWater



# Start two pointers L and R at oppisite end of array
# Calculate area = (r - l) * min(h[r], h[l])
# Update the max if area is more than the curr max
# Move pointer on smaller height forward
# Return max
