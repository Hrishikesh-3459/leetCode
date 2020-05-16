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