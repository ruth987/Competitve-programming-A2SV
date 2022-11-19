class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one, two = 0, 0
        for i in range(len(nums1)-m):
            nums1.pop()
        while two < n:
            if one==len(nums1):
                for item in nums2[two:]:
                    nums1.append(item)
                break
            if nums1[one]<=nums2[two]:
                one+=1
            else:
                nums1.insert(one, nums2[two])
                one+=1
                two+=1