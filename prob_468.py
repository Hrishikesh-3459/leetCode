class Solution:
    def validIPAddress(self, IP: str) -> str:
        # IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
        if IP.count('.') == 3:
            x = IP.split('.')
            if len(x) != 4:
                return "Neither"
            for i in x:
                if len(i) not in range(1, 4):
                    return "Neither"
                if not i.isdigit():
                    return "Neither"
                if i[0] == '0' and len(i) != 1:
                    return "Neither"
                if int(i) > 255 or int(i) < 0:
                    return "Neither"
            return "IPv4"
        elif IP.count (':') == 7:
            x = IP.split(':')
            print(x)
            if len(x) != 8:
                return "Neither"
            hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            for i in x:
                if len(i) == 0 or len(i) > 4:
                    return "Neither"
                for j in i:
                    if j.isalpha():
                        if j.upper() not in hexa:
                            return "Neither"
                    elif j.isdigit():
                        if j not in hexa:
                            return "Neither"
                    else:
                        if j not in hexa:
                            return "Neither"
            return "IPv6"
        return "Neither"
