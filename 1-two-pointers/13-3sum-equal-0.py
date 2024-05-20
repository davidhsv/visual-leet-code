from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        for i in range(0, len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    solutions.append([nums[i], nums[left], nums[right]])
                    tmp = nums[left]
                    left = left + 1
                    while left < right and tmp == nums[left]:
                        left = left + 1

                    tmp = nums[right]
                    right = right - 1
                    while left < right and tmp == nums[left]:
                        right = right - 1

                elif sum < target:
                    left = left + 1
                elif sum > target:
                    right = right - 1
        return solutions


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, -1, -1, 0, 1, 2]))