class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = []
        x = ""
        for i in s:
            if (i in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']):
                vow.append(i)
        k = 0
        r_vow = vow[::-1]
        for i in s:
            if (i not in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']):
                x += i
            else:
                x += r_vow[k]
                k += 1
                
        return x
    
