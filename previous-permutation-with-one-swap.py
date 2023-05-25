class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        left = n - 2

        # Find the first decreasing element from the right
        while left >= 0 and arr[left] <= arr[left + 1]:
            left -= 1

        # If there's no decreasing element, it's already the smallest permutation
        if left == -1:
            return arr

        # Find the largest element smaller than arr[left] to its right
        right = n - 1
        while arr[right] >= arr[left]:
            right -= 1

        # Find the rightmost occurrence of the element to swap
        while arr[right] == arr[right - 1]:
            right -= 1
        
        # Swap arr[left] and arr[right]
        arr[left], arr[right] = arr[right], arr[left]
        
        return arr