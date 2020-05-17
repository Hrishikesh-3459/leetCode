class Solution:
    def toLowerCase(self, str: str) -> str:
        out = ""
        for i in str:
            if (ord(i) in range(97, 123)):
                out += i
            elif (ord(i) in range(65, 91)):
                out += chr(ord(i) + 32)
            else:
                out += i

        return(out)
