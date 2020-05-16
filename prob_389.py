<<<<<<< HEAD
def findTheDifference(s, t):
    x =list(t)
    for i in s:
        x.remove(i)

    print(x[0])

findTheDifference('a', 'aa')
=======
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x =list(t)
        for i in s:
            x.remove(i)

        return(x[0])
            
>>>>>>> c342f33c5f94635b5901867b435c2165820ee334
