class Solution:
    def indexPairs(self, text, words):
        ans = []
        for i in words:
            tmp = self.find_indices(i, text)
            ans.extend(tmp)
        return sorted(ans)
    
    def find_indices(self, word, text):
        ch = list(word)
        n = len(word)
        start = 0
        end = start + n
        temp = []
        q = list(text[start:end])
        if q == ch:
            st = end - n
            temp.append([st, end - 1])
        while end < len(text):
            q.pop(0)
            q.append(text[end])
            end += 1
            if q == ch:
                st = end - n
                temp.append([st, end - 1])
        return temp