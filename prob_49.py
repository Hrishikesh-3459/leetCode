import copy
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
        import copy
        # ans = []
        # while strs:
        #     x = strs.pop(0)
        #     tmp = [x]
        #     for i in strs:
        #         if (sorted(i) == sorted(x)):
        #             tmp.append(i)
        #     t = copy.copy(tmp)
        #     ans.append(t)
        #     strs.append(x)
        #     for i in tmp:
        #         strs.remove(i)
        #     tmp.clear()
        # return ans 
