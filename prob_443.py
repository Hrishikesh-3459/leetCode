class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(" ")
        x = []
        i = 0
        count = 1
        while True:
            if (chars[i] == chars[i+1]):
                count += 1
            else:
                x.append(chars[i])
                if (count < 10 and count != 1):
                    x.append(str(count))
                if (count >= 10):
                    temp = str(count)
                    for j in temp:
                        x.append(j)
                count = 1

            if i + 1 == len(chars) - 1:
                break
            i += 1
        chars.clear()
        for i in x:
            chars.append(i)

        return(len(chars))
