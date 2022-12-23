class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_start = m-1
        right_start = n-1
        up = len(nums1)-1

        if len(nums1) == n:
            for i in range(n):
                nums1[i] = nums2[i]

        while left_start >= 0 and right_start >= 0:
            if nums1[left_start] > nums2[right_start]:
                nums1[up] = nums1[left_start] 
                left_start-=1
                up -=1
            elif nums1[left_start] <= nums2[right_start]:
                nums1[up] = nums2[right_start] 
                right_start-=1
                up -=1
        while right_start >= 0:
            nums1[up] = nums2[right_start] 
            right_start-=1
            up -=1
                