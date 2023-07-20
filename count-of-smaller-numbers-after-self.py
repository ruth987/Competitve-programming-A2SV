from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        optimized solution
        """
        s = SortedList()
        ans = []
        for i in range(len(nums)-1, -1, -1):
            a = bisect.bisect_left(s, nums[i])
            ans.append(a)
            s.add(nums[i])
        
        return ans[::-1]