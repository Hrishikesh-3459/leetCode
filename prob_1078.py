class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        x = text.split()
        for i in range(1, len(x)):
            if (x[i - 1] == first and x[i] == second):
                if (i + 1 < len(x)):
                    ans.append(x[i + 1])
        return ans
