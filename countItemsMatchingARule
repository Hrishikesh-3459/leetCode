class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            check = 0
        if ruleKey == "color":
            check = 1
        if ruleKey == "name":
            check = 2
        ans = 0
        for item in items:
            if item[check] == ruleValue:
                ans += 1
        return ans
