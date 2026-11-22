class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search the smaller array to keep time O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2        # Elements taken from nums1
            j = total_left - i           # Elements taken from nums2

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # Valid partition found
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0

            # Too many elements taken from nums1; move partition left
            elif left1 > right2:
                high = i - 1
            # Too few elements taken from nums1; move partition right
            else:
                low = i + 1

        return 0.0