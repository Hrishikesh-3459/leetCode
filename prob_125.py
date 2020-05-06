def isPalindrome(s: str) -> bool:
    if (len(s) == 0 or len(s) == 1):
        return(True)
    palin = ""
    for i in s:
        if(i.isalnum()):
            palin += i.lower()
    if (palin == palin[::-1]):
        return True
    else:
        return False