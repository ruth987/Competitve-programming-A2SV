class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        def pos_odds(num):
            odds = []
            for number in range(2, num+1):
                if number%2 != 0:
                    odds.append(number)
            return odds
        
        result_sum = sum(arr)
        oddA = pos_odds(len(arr))
        
        for i in range(1, len(arr)):
            arr[i]+=arr[i-1]
        
        for odd in oddA:
            before = 0
            start, end = 0, odd-1
            while end<len(arr):
                result_sum+=(arr[end]-before)
                before = arr[start]
                start+=1
                end+=1
        return result_sum
        
            
            
                
            
            
            

        