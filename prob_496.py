class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        for i in nums1:
            flag = False
            for j in nums2[nums2.index(i):]:
                if (j > i):
                    flag = True
                    x.append(j)
                    break
            if (flag == False):
                x.append(-1)
        return x
