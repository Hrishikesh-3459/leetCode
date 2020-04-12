def isPalindrome(x):
        st = str(x)
        rev = st[::-1]
        if(x<0):
            return False
        if(int(rev) == x):
            return True
        else:
            return False
print(isPalindrome(-123))