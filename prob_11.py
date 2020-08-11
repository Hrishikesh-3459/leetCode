class Solution:
    def maxArea(self, height):
        ans = -1
        left = 0
        right = len(height) - 1
        while left < right:
            smol = min(height[left], height[right])
            cur = smol * (right - left)
            ans = max(ans, cur)
            if smol == height[left]:
                left += 1
            else:
                right -= 1
        return ans
        