class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        a = 0
        b = 0
        c = len(nums1) - 1

        while a < m:
            if nums1[a] <= nums2[b]:
                a += 1
            else:
                swapPositions(nums1, nums1, a, c)
                swapPositions(nums1, nums2, a, b)
                a += 1
                c -= 1
                b += 1
        while


def swapPositions(nums1, nums2, pos1, pos2):
    temp = nums1[pos1]
    nums1[pos1] = nums2[pos2]
    nums2[pos2] = temp


def main():
    nums1 = [1, 2, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0]
    m = 5
    nums2 = [2, 3, 3, 8, 9, 10, 11]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':
    main()