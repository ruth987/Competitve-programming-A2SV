class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mydict = defaultdict(int)
        for money in bills:
            if money == 5:
                mydict[5] += 1
            elif money == 10:
                mydict[10] += 1
                if mydict[5]:
                    mydict[5] -= 1
                else:
                    return False
            else: # money == 20
                mydict[20] += 1
                if mydict[10] and mydict[5]:
                    mydict[10] -= 1
                    mydict[5] -= 1
                elif mydict[5] >= 3:
                    mydict[5] -= 3
                else:
                    return False
        return True