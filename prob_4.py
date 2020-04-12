def findMedianSortedArrays(nums1, nums2):
    x = nums1 + nums2
    j = sorted(x)
    print(j)
    if((len(j)%2) == 1):
        cen = int(len(j)/2)
        return(j[cen])
    else:
        cen_1 = int(len(j)/2)
        cen_2 = int(len(j)/2) - 1
        jam = (j[cen_1] + j[cen_2])/2
        return(jam)
print(findMedianSortedArrays([1,3], [2]))