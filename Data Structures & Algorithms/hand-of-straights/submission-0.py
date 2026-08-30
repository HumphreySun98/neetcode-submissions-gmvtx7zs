class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize :
            return False


        count = Counter(hand)

        for x in sorted(count):
            need = count[x]
            if need == 0:
                continue


            for v in range(x,x+groupSize):
                if count[v] < need:
                    return False

                count[v] -= need



        return True
        