class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        rems = []
        remg = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                rems.append(secret[i])
                remg.append(guess[i])
        B = 0
        for i in remg:
            if i in rems:
                B += 1
                rems.remove(i)
        ans = f"{A}A{B}B"
        return ans