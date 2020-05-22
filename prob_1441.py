class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        a_arr = []
        for i in range(1, n+1):
            if (a_arr == target):
                break
            a_arr.append(i)
            ans.append("Push")
            if (a_arr[-1] not in target):
                ans.append("Pop")
                a_arr.pop()
        return ans
