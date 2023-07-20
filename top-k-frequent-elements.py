class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        check = 0
        mydict = {}
        for number in nums:
            if number not in mydict:
                mydict[number]=1
            else:
                mydict[number]+=1
        mydict  = (sorted(mydict.items(), key=lambda item: item[1]))[::-1]

        for i in mydict:
            ans.append(i[0])
            check += 1
            if check == k:
                break
        return ans