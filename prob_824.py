class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        vowels = 'AaEeIiOoUu'
        ans = []
        for i, w in enumerate(words):
            if w[0] in vowels:
                val = w + "ma" + ('a' * (i + 1))
                ans.append(val)
            else:
                val = w[1:] + w[0] + "ma" + ('a' * (i + 1))
                ans.append(val)
        return ' '.join(ans)
