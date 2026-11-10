#Partition understanding 

text = "This is a sample text for partitioning."

result = text.partition("sample")
print(result)

#Chatgpt answer given for the question, it works
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        while left <= right:

            # Find partition positions
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Find the four boundary values
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Even number of elements
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) +
                            min(minRight1, minRight2)) / 2

                # Odd number of elements
                else:
                    return float(max(maxLeft1, maxLeft2))

            # Move binary search left
            elif maxLeft1 > minRight2:
                right = partition1 - 1

            # Move binary search right
            else:
                left = partition1 + 1


