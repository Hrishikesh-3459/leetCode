class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        di = {}
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        k = 97
        for i in morse:
            di[chr(k)] = i
            k += 1
        ans = []
        count = 0
        for i in words:
            letters = ""
            for j in i:
                letters += di[j]
            if (letters not in ans):
                ans.append(letters)
        return len(ans)
        
