class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = collections.Counter(nums1)
        nums2_dict = collections.Counter(nums2)
        
        answer, saved = [], []
        sav = set()
        
        for number in nums1:
            if number not in sav and number in nums1_dict and number in nums2_dict:
                sav.add(number)
                saved.append(number) 
        
        for num in saved:
            for i in range(min(nums1_dict[num], nums2_dict[num])):
                answer.append(num)
                
        return answer
    
    