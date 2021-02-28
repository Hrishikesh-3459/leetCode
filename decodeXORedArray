class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in encoded:
            tmp = i ^ ans[-1]
            ans.append(tmp)
        return ans
