class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        it has to increase up to some point.
        it has to decrease from that point to the end.

        if both the numbers arenot smaller that means one of them is bigger: 
             so take the bigger for the next search
        [0,5,10,2]
        """
        left, right = 1, len(arr)-2
        while left <= right:
            mid = (left+right)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            
            elif arr[mid] < arr[mid+1]:
                left = mid+1
            elif arr[mid] < arr[mid-1]:
                right = mid-1
        