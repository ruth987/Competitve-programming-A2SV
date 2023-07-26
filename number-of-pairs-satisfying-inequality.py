class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        for i in range(len(nums2)):
            arr.append(nums1[i] - nums2[i])
        count = 0
        def merge(arr):
            nonlocal count 
            if len(arr) == 1:
                return arr
            left = merge(arr[:len(arr)//2])
            right = merge(arr[len(arr)//2:])

            for i in left:
                count += len(right) - bisect_left(right, (i - diff))
            
            ans = []
            l = r = 0
            while r < len(right) or l < len(left):
                
                if r >= len(right) or ((l < len(left)) and (left[l] <= right[r])):
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            return ans 
        merge(arr)
        return count