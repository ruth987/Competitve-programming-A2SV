class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        aset = set()
        for num in arr:
            if num/2 in aset or num*2 in aset:
                    return True
            if num not in aset:
                aset.add(num)
            
        return False
            