class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        x = sorted(words, key = len)
        st = ""
        for i in x:
            st += i.lower() + " "
        return st.capitalize().rstrip()
        
