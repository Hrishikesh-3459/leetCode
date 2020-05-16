<<<<<<< HEAD
def intersect(nums1, nums2):
    out = []
    for i in nums1:
        print(i)
        if (i in nums2):
            out.append(i)
            # nums1.remove(i)
            nums2.remove(i)
    return (out)

print(intersect([1,2,2,1], [2,2]))
=======
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for i in nums1:
            if (i in nums2):
                out.append(i)
                # nums1.remove(i)
                nums2.remove(i)
        return (out)
>>>>>>> c342f33c5f94635b5901867b435c2165820ee334
