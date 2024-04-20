def isPalindrome(x):
        new_num = 0
        old_num = x
        ite = 1
        while (x > 0):
            rem = x % 10
            if (rem == 0 and ite == 1):
                return False
            quo = x // 10
            new_num = rem + (new_num * 10)
            ite = ite * 10
            x = quo
        print(new_num)
        return new_num == old_num

print(isPalindrome(121))