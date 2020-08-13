class Solution:
    def confusingNumber(self, N):
        same = '018'
        diff = '69'
        invalid = '23457'
        ans = ''
        for i in str(N):
            if i in invalid:
                return False
            if i in same:
                ans += i
            else:
                if i == '6':
                    ans += '9'
                else:
                    ans += '6'
        if int(ans[::-1]) == N:
            return False
        return True