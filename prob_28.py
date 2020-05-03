def strStr(self, haystack, needle):
    if(len(needle) == 0):
        return 0
    return(haystack.find(needle))