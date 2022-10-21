class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydict = {}
        
        for idx, number in enumerate(nums):
            if number not in mydict:
                mydict[number] = idx
            else:
                if (idx-mydict[number]) <= k:
                    return True
                mydict[number] = idx
        return False
        