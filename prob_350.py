class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for i in nums1:
            if (i in nums2):
                out.append(i)
                # nums1.remove(i)
                nums2.remove(i)
        return (out)
