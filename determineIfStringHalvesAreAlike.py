class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        first = 0
        second = 0
        half = len(s) // 2
        for i, j in zip(s[:half], s[half:]):
            if i in vowels:
                first += 1
            if j in vowels:
                second += 1
        return first == second
