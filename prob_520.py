class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (word.isupper()):
            return True
        if (word.islower()):
            return True
        if (word[0].isupper()):
            for i in word[1:]:
                if (i.isupper()):
                    return False
            return True
        return False
