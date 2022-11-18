class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer = []
        
        for number in set1:
            if number in set2:
                answer.append(number)
        
        return answer
    