class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n, ans = len(nums), []
        mydict = collections.Counter(nums)

        for item in mydict.items():
            if item[1] > int(n/3):
                ans.append(item[0])
        return ans
        