from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1

        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([2, 4, 1]))