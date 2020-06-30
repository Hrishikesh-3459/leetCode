class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            flag = True
            di = {}
            for j, let in enumerate(pattern):
                if let in di:
                    if di[let] != word[j]:
                        flag = False
                        break
                else:
                    if word[j] in di.values():
                        flag = False
                        break
                    else:
                        di[let] = word[j]
            if flag == True:
                ans.append(word)
        return ans
