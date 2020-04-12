def lengthOfLongestSubstring(s):
        x = []
        count = 0
        if(len(s) == 1):
            return(1)
        for i in s:
            if (i not in x): 
                x.append(i)
                temp_count = len(x)
                print("1", x)
                if(temp_count > count):
                    count = temp_count
            else:
                temp_count = len(x)
                if(temp_count > count):
                    count = temp_count
                x = x[x.index(i) + 1 : ]
                x.append(i)
                print(x)
        return(count)
print(lengthOfLongestSubstring("aabaabcbb"))

# aabaabcbb 
