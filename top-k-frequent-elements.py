class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] += 1
        
        s_dict = sorted(mydict.items(), key = lambda item: item[1], reverse = True)
        # print(s_dict)
        ans = []
        for i in range(k):
            ans.append(s_dict[i][0])
        
        return ans