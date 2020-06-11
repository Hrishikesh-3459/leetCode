class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        if not arr:
            return 
        di = {}
        for i in sorted(arr):
            val = '{0:b}'.format(i)
            x = val.count('1')
            if x in di:
                di[x].append(i)
            else:
                di[x] = [i]
        ans = []
        for i in sorted(di):
            ans.extend(di[i])
        return ans
