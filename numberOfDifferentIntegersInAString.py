class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in range(97, 123):
            word = word.replace(chr(i), " ")
        letters = set()
        for i in word.split():
            if set(i) != "0":
                tmp = i.lstrip("0")
                letters.add(tmp)
            else:
                letters.add("0")
        return (len(letters))
