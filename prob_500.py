class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        ans = []
        for word in words:
            f1 = True
            f2 = True
            f3 = True
            for letter in word.lower():
                if (letter not in row1):
                    f1 = False
                    break
            if(f1 == True):
                ans.append(word)
                continue
            for letter in word.lower():
                if (letter not in row2):
                    f2 = False
                    break
            if(f2 == True):
                ans.append(word)
                continue
            for letter in word.lower():
                if (letter not in row3):
                    f3 = False
                    break
            if(f3 == True):
                ans.append(word)
                continue
            
        return ans
            
