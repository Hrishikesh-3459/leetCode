class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for i in words:
            flag = 0
            for j in i:
                if (i.count(j) <= chars.count(j)):
                    flag += 1
            if (flag == len(i)):
                count += len(i)




        return count
        
