import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        di = {}
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c," ") 
        for word in paragraph.split():
            if (word.lower() in di):
                di[word.lower()] += 1
            else:
                di[word.lower()] = 1
        freq = 0
        ans = ""
        for i in di:
            if (i in banned):
                continue
            if (di[i] > freq):
                freq = di[i]
                ans = i
        return ans
            
            
        
