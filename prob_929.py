class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        local = []
        for email in emails:
            loc, dom = email.split('@')
            if '.' in loc:
                loc = loc.replace('.', '')
            if '+' in loc:
                ind = loc.index('+')
                loc = loc[:ind]
            fin = loc + '@' + dom
            if fin not in local:
                local.append(fin)
        print(local)
        return len(local)
                    
