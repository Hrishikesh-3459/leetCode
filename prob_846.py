class Solution:
    def isNStraightHand(self, hand, W):
        if len(hand) % W != 0:
            return False
        while hand:
            smol = min(hand)
            hand.remove(smol)
            tmp = [smol]
            for i in range(W-1):
                val = tmp[-1]
                if (val + 1) not in hand:
                    return False
                tmp.append(val + 1)
                hand.remove(val + 1)
        return True