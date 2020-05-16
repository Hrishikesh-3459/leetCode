class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lol = list(magazine)
        for i in ransomNote:
            if (i not in lol):
                return False
            lol.remove(i)
        return True
