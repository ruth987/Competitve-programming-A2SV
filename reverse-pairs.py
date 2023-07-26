class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0

        def merge(left, right):
            nonlocal cnt              
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:               
                    i += 1                              
                else:
                    cnt += len(left)-i                 
                    j += 1                             

            return sorted(left+right)                  


        def mergeSort(A):
            if len(A) == 1:                            
                return A
            mid=(len(A)) // 2
            return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))     
            
        mergeSort(nums)
        return cnt